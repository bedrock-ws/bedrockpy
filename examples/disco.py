import logging
import os

from bedrock.context import ConnectContext, ReadyContext, DisconnectContext
from bedrock.server import Server

logging.basicConfig(level=logging.DEBUG)

app = Server()

@app.server_event
async def ready(ctx: ReadyContext) -> None:
    print(f"Ready @ {ctx.host}:{ctx.port}")

@app.server_event
async def connect(ctx: ConnectContext) -> None:
    print("Connect")

@app.server_event
async def disconnect(ctx: DisconnectContext) -> None:
    print("Disconnect")

app.start(os.getenv("IP") or "localhost", 6464)
