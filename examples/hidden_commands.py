"""
This example tests commands that might be usable only via a websocket
connection.

querytarget: success, returns data like position of target
geteduclientinfo: failure, "no cheats enabled in this world"
getlocalplayername: success, returns player name that is connected to the server
"""

import logging
import os

from bedrock.consts import NAME
from bedrock.context import PlayerMessageContext
from bedrock.server import Server
from bedrock.utils import rawtext

logging.basicConfig(level=logging.DEBUG)

app = Server()

@app.game_event
async def player_message(ctx: PlayerMessageContext) -> None:
    if ctx.sender == NAME:
        return
    if ctx.message == "getlocalplayername":
        res = await ctx.server.run("getlocalplayername")
        print(repr(res))
        await ctx.server.run(f"tellraw @a {rawtext(repr(res))}")
    elif ctx.message == "geteduclientinfo":
        res = await ctx.server.run("geteduclientinfo")
        print(repr(res))
        await ctx.server.run(f"tellraw @a {rawtext(repr(res))}")
    elif ctx.message == "querytarget":
        res = await ctx.server.run("querytarget @a")
        print(repr(res))
        await ctx.server.run(f"tellraw @a {rawtext(repr(res))}")

app.start(os.getenv("IP") or "localhost", 6464
