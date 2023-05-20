import logging
import os

from bedrock.consts import NAME
from bedrock.context import PlayerMessageContext, ReadyContext
from bedrock.server import Server

logging.basicConfig(level=logging.DEBUG)

app = Server()

@app.server_event
async def ready(ctx: ReadyContext) -> None:
    print(f"Ready @ {ctx.host}:{ctx.port}")

@app.game_event
async def player_message(ctx: PlayerMessageContext) -> None:
    if ctx.sender != NAME and ctx.message == "overflow":
        for i in range(150):
            await ctx.server.run(f"say {i}")

app.start(os.getenv("IP") or "localhost", 6464)
