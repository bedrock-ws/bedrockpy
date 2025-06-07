from collections.abc import Callable, Coroutine
from typing import Any, Generic, TypeVar

from attrs import define

from .context import Context, GameContext, ServerContext

ContextType = TypeVar("ContextType", bound=Context)
EventHandler = Callable[[ContextType], Coroutine[Any, Any, None]]


@define
class Event(Generic[ContextType]):
    name: str
    handler: EventHandler[ContextType]

    async def __call__(self, ctx: ContextType, /) -> None:
        return await self.handler(ctx)


@define
class GameEvent(Event[GameContext]):
    pass


@define
class ServerEvent(Event[ServerContext]):
    pass
