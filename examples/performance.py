"""
A message triggers a loop which places a lot of blocks to see how fast it works.
"""

import logging
import os
import time

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
    if ctx.sender != NAME and ctx.message == "performance":
        now = time.time()
        n = 1_000
        for i in range(n):
            await ctx.server.run(f"say iteration {i}", wait=False)
        print(f"took {time.time() - now}s to run {n} commands")


app.start(os.getenv("IP") or "0.0.0.0", 6464)
