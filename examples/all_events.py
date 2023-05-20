import logging
import os

from bedrock.consts import GAME_EVENTS, NAME
from bedrock.context import GameContext, ReadyContext
from bedrock.events import GameEvent
from bedrock.server import Server

logging.basicConfig(level=logging.DEBUG)

app = Server()

@app.server_event
async def ready(ctx: ReadyContext) -> None:
    print(f"Ready @ {ctx.host}:{ctx.port}")

for name in GAME_EVENTS:
    async def handler(ctx: GameContext) -> None:
        print(ctx._data)
    app.add_game_event(GameEvent(name, handler))

app.start(os.getenv("IP") or "localhost", 6464)
