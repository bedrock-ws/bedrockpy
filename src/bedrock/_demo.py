"""Demo script to quickly test if everything is set up correctly.

This demo exists so one does not have to write a script just to find out that
the device is not supported or a similar issue. It prints text to the console
as soon as the server is ready to be used and displays a message in the game's
chat when a connection has been successfully established.
"""

import socket

from .context import ConnectContext, ReadyContext
from .server import Server
from .utils import rawtext


def get_ip() -> str:
    """Returns the private IP address."""
    return socket.gethostbyname(socket.gethostname())


app = Server()


@app.server_event
async def ready(ctx: ReadyContext) -> None:
    print(
        f"The server has been started. You may now type "
        f"`/connect {ctx.host}:{ctx.port}` in the game."
    )


@app.server_event
async def connect(ctx: ConnectContext) -> None:
    message = "Yeah! It works."
    await ctx.server.run(f"tellraw @a {rawtext(message)}")
    print(f"You should now see {message!r} in the game chat.")


if __name__ == "__main__":
    app.start(get_ip(), 6464)
