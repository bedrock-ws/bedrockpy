import asyncio
from collections.abc import Mapping
import json
import logging
from typing import Any, Literal, overload
import uuid
import warnings

from attrs import define, field
import convert_case  # type: ignore

try:
    import uvloop  # type: ignore
except ImportError:
    pass
from websockets import server as wss
from websockets.exceptions import ConnectionClosedError

from . import consts, context, events, response
from .request import CommandRequest
from .response import CommandResponse


logger = logging.getLogger(__name__)


@define
class Server:
    """
    A server handles the connection to a client in the game.
    """

    _game_event_handlers: list[events.GameEvent] = field(init=False, factory=list)
    _server_event_handlers: list[events.ServerEvent] = field(init=False, factory=list)
    _loop: asyncio.AbstractEventLoop | None = field(init=False, default=None)
    _ws: wss.WebSocketServerProtocol | None = field(init=False, default=None)
    _is_connected: bool = field(init=False, default=False)
    _command_processing_semaphore: asyncio.BoundedSemaphore = field(
        init=False,
        factory=lambda: asyncio.BoundedSemaphore(consts.MAX_COMMAND_PROCESSING),
    )
    _requests: list[CommandRequest] = field(init=False, factory=list)

    def server_event(self, fn: events.EventHandler, /) -> events.ServerEvent:
        """Convenient way of adding a server event.

        The decorated function name must match the name of the event to listen to.
        It takes one positional argument which is an instance of
        :class:`context.ServerContext` of the event.

        Examples
        --------

        .. code-block:: python

            ...
            @app.server_event
            async def ready(ctx):
                print(f"Ready @ {ctx.host}:{ctx.port}")

        Parameters
        ----------
        fn
            The decorated function.

        Returns
        -------
        events.ServerEvent
            The function turned into a :class:`events.ServerEvent`.
        """
        event = events.ServerEvent(fn.__name__, fn)
        self.add_server_event(event)
        return event

    def add_server_event(self, event: events.ServerEvent) -> None:
        """Adds a server event to the game event handlers."""
        self._server_event_handlers.append(event)

    def remove_server_event(self, event: events.ServerEvent) -> None:
        """Removes a server event from the game event handlers.

        Raises
        ------
        ValueError
            Event is not registered.
        """
        self._server_event_handlers.remove(event)

    def game_event(self, fn: events.EventHandler, /) -> events.GameEvent:
        """Convenient way of adding a game event.

        The decorated function name must match the name of the event to listen to.
        It takes one positional argument which is an instance of
        :class:`context.GameContext` of the event.

        Examples
        --------

        .. code-block:: python

            ...
            @app.server_event
            async def player_message(ctx):
                ctx.reply("Hello World!")

        Parameters
        ----------
        fn
            The decorated function.

        Returns
        -------
        events.GameEvent
            The function turned into a :class:`events.GameEvent`.
        """
        event = events.GameEvent(fn.__name__, fn)
        self.add_game_event(event)
        return event

    def add_game_event(self, event: events.GameEvent) -> None:
        """Adds a game event to the game event handlers."""
        self._game_event_handlers.append(event)

    def remove_game_event(self, event: events.GameEvent) -> None:
        """Removes a game event from the game event handlers.

        Raises
        ------
        ValueError
            Event is not registered.
        """
        self._game_event_handlers.remove(event)

    @overload
    async def send(
        self,
        header: dict[str, Any],
        body: dict[str, Any],
        *,
        wait: Literal[True] = True,
    ) -> CommandResponse:
        ...

    @overload
    async def send(
        self,
        header: dict[str, Any],
        body: dict[str, Any],
        *,
        wait: Literal[False],
    ) -> None:
        ...

    async def send(
        self,
        header: dict[str, Any],
        body: dict[str, Any],
        *,
        wait: bool = True,
    ) -> CommandResponse | None:
        """Sends data to the client.

        Parameters
        ----------
        header
            The header data for the request.

        body
            The body data for the request.

        wait
            Waits for a response when awaiting.

        Returns
        -------
        CommandResponse
            The response of the request wrapped in a :external+python:py:class:`asyncio.Future`.
        """
        self._assert_connected()
        assert self._ws is not None
        assert self._loop is not None

        identifier = uuid.uuid4()
        data = {
            "header": header | {"version": 1, "requestId": str(identifier)},
            "body": body,
        }

        request = CommandRequest(
            identifier=identifier, data=data, response=self._loop.create_future()
        )

        await self._command_processing_semaphore.acquire()
        
        logger.debug("sending data ...")
        await self._ws.send(json.dumps(data))
        logger.debug("sent data ...")

        self._requests.append(request)
        
        if wait:
            logger.debug("waiting for response ...")
            res = await request.response
            logger.debug("got response")
            return res
        return None

    async def subscribe(self, event_name: str) -> CommandResponse:
        """Subscribes to a game event.

        Game events are automatically subscribed to when a listener is added
        with :meth:`add_game_event` or :meth:`game_event` so there is usually
        no need to manually use this method.

        Parameters
        ----------
        event_name
            The name of the game event to subscribe to.
        """
        self._assert_connected()

        return await self.send(
            header={"messageType": "commandRequest", "messagePurpose": "subscribe"},
            body={"eventName": convert_case.pascal_case(event_name)},
        )

    async def unsubscribe(self, event_name: str) -> CommandResponse:
        """Unsubscribes to a game event.

        Parameters
        ----------
        event_name
            The name of the game event to unsubcribe.
        """
        self._assert_connected()

        return await self.send(
            header={"messageType": "commandRequest", "messagePurpose": "unsubscribe"},
            body={"eventName": convert_case.pascal_case(event_name)},
        )

    @overload
    async def run(
        self,
        command: str,
        *,
        version: str | list[str] | None = None,
        wait: Literal[True] = True,
    ) -> CommandResponse:
        ...

    @overload
    async def run(
        self,
        command: str,
        *,
        version: str | list[str] | None = None,
        wait: Literal[False]
    ) -> None:
        ...

    async def run(
        self,
        command: str,
        *,
        version: str | list[str] | None = None,
        wait: bool = True,
    ) -> CommandResponse | None:
        """Executes a Minecraft command.

        .. note:: The leading slash (``/``) may be omitted.

        Parameters
        ----------
        command
            The command to execute. For example ``setblock 10 10 10 stone``.

        version
            The Minecraft version the command syntax relies on. This can
            usually be ignored.

        wait
            Waits for a response when awaiting.
        """
        version = version or consts.MINECRAFT_VERSION
        command = command.removeprefix("/")
        return await self.send(
            header={
                "messageType": "commandRequest",
                "messagePurpose": "commandRequest",
            },
            body={
                "version": version,
                "commandLine": command,
                "origin": {"type": "player"},
            },
            wait=wait,
        )  # type: ignore

    def _dispatch_server_event(self, name: str, ctx: context.ServerContext) -> None:
        assert self._loop is not None
        for event in self._server_event_handlers:
            if event.name == name:
                self._loop.create_task(event(ctx))

    def start(self, host: str, port: int) -> None:
        """Starts the server.

        Parameters
        ----------
        host
            The host to run the server on.

        port
            The port to run the server on.
        """
        runner: asyncio.Runner | None = None
        server = wss.serve(self._websocket_handler, host=host, port=port)
        self._loop = asyncio.get_event_loop()
        """
        if sys.version_info >= (3, 11):
            try:
                loop_factory = uvloop.new_event_loop
            except NameError:
                loop_factory = asyncio.new_event_loop
            runner = asyncio.Runner(loop_factory=loop_factory)
            self._loop = runner.get_loop()
            self._loop.run_until_complete(server)
        else:
            try:
                uvloop.install()
            except NameError:
                pass
            self._loop = asyncio.new_event_loop()
        """
        self._loop.run_until_complete(server)
        self._dispatch_server_event(
            "ready", context.ReadyContext(self, host=host, port=port)
        )
        try:
            self._loop.run_forever()
        except KeyboardInterrupt as e:
            raise KeyboardInterrupt from None
        finally:
            self._dispatch_server_event("disconnect", context.DisconnectContext(self))
            for t in asyncio.tasks.all_tasks(self._loop):
                t.cancel()
            self._is_connected = False
            self._loop.close()
            if runner is not None:
                runner.close()

    def close(self) -> None:
        """Closes the server."""
        if self._ws is None:
            raise RuntimeError("server is not running")
        assert self._loop is not None
        self._loop.create_task(self._ws.close())

    def is_ready(self) -> bool:
        """Returns ``True`` when the server is ready to establish a connection."""
        return self._ws is not None and self._ws.ws_server.is_serving()

    def is_connected(self) -> bool:
        """Returns ``True`` when the server is connected to a client."""
        return self._is_connected

    def _assert_connected(self) -> None:
        """
        Raises
        ------
        RuntimeError
            The server is not connected to a client.
        """
        if not self.is_connected():
            raise RuntimeError("server is not connected to a client")

    async def _websocket_handler(self, server: wss.WebSocketServerProtocol) -> None:
        logger.debug("handling ws")

        self._ws = server
        self._is_connected = True
        self._dispatch_server_event("connect", context.ConnectContext(self))

        for event in self._game_event_handlers:
            identifier = uuid.uuid4()
            await self.send(                
                header = {
                    "messageType": "commandRequest",
                    "messagePurpose": "subscribe",
                    "version": 1,
                    "requestId": str(identifier),
                },
                body = {"eventName": convert_case.pascal_case(event.name)},
                wait=False
            )

        try:
            async for message in self._ws:
                logger.debug("processing data ...")
                data = json.loads(message)
                await self._process_data(data)
                logger.debug("processed data")
        except ConnectionClosedError:
            self._dispatch_server_event("disconnect", context.DisconnectContext(self))
            self._is_connected = False

    async def _process_data(self, data: Mapping[str, Any]) -> None:
        assert self._loop is not None

        header = data["header"]
        body = data["body"]
        is_response = header.get("messagePurpose") == "commandResponse"
        is_error = header.get("messagePurpose") == "error"
        
        event_name: str | None
        if (name := header.get("eventName")) is not None:
            event_name = convert_case.snake_case(name)
        else:
            event_name = None

        logger.debug(f"{self._game_event_handlers}")
        for event in self._game_event_handlers:
            if event.name == event_name:
                logger.debug("triggering event ...")
                try:
                    ctx = context.get_game_context(event_name)(self, body)
                except KeyError:
                    # from pprint import pprint
                    # pprint(event_name)
                    # pprint(body)
                    warnings.warn(f"unknown event name {event_name!r}", RuntimeWarning)
                    ctx = context.GameContext(self, body)
                self._loop.create_task(event(ctx))

        if is_response:
            self._command_processing_semaphore.release()
            identifier = uuid.UUID(header["requestId"])
            for req in self._requests:
                if req.identifier == identifier:
                    logger.debug(f"got response for {identifier!r}")
                    res = response.CommandResponse.parse(data)
                    req.response.set_result(res)
                    self._requests.remove(req)
