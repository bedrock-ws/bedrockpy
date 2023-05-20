"""
Demo script for quickly test if everything is set up correctly.
"""

import socket

from .context import ConnectContext, ReadyContext
from .server import Server
from .utils import rawtext

def get_ip() -> str:
    """Returns the IP address."""
    return socket.gethostbyname(socket.gethostname())

app = Server()

@app.server_event
async def ready(ctx: ReadyContext) -> None:
    print(f"The server has been started. You may now type "
          f"`/connect {ctx.host}:{ctx.port}` in the game.")

@app.server_event
async def connect(ctx: ConnectContext) -> None:
    message = "Yeah! It works."
    await ctx.server.run(f"tellraw @a {rawtext(message)}")
    print(f"You should now see {message!r} in the game chat.")

if __name__ == "__main__":
    app.start(get_ip(), 6464)
