from collections.abc import Callable, Coroutine
from typing import TypeVar

from attrs import define

from .context import Context

ContextType = TypeVar("ContextType", bound=Context)
EventHandler = Callable[[ContextType], Coroutine]  # TODO: specify coro types


@define
class Event:
    name: str
    handler: EventHandler

    async def __call__(self, ctx: Context, /) -> None:
        return await self.handler(ctx)


@define
class GameEvent(Event):
    pass


@define
class ServerEvent(Event):
    pass
