"""
This example is used to figure out what happens when an event should
be triggered while another one is running.

Send a message in the chat which will trigger a lot of messages beeing
sent by the server. In the meantime, destroy a block and a title should
appear.
"""

import logging
import os

from bedrock.consts import NAME
from bedrock.context import BlockBrokenContext, PlayerMessageContext, ReadyContext
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

@app.game_event
async def block_broken(ctx: BlockBrokenContext):
    await ctx.server.run("title @a title Hello!")

app.start(os.getenv("IP") or "localhost", 6464)
