<p align="center">
  <h1 align="center">bedrockpy</h1>
  <p align="center">
    Minecraft: Bedrock Edition Websocket Server
  </p>
</p>

<!-- start brief-hook -->

*bedrockpy* lets you create a websocket server that is able to interact
with a player in a Minecraft game. As the name suggests: this project
only works with the "Minecraft: Bedrock Edition".

[![Documentation Status](https://readthedocs.org/projects/bedrockpy/badge/?version=latest)](https://bedrockpy.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/github/license/bedrock-ws/bedrockpy?style=flat-square)](https://github.com/bedrock-ws/bedrockpy/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/bedrockpy?style=flat-square)](https://pypi.org/project/bedrockpy)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/bedrockpy?style=flat-square)](https://pypi.org/project/bedrockpy)


## Quick Links

* 📦 [PyPI](https://pypi.org/project/bedrockpy)
* 📖 [Docs](https://bedrockpy.readthedocs.io/)
* 🐍 [Repo](https://github.com/bedrock-ws/bedrockpy/)


## "Show me some Code"

> Code says more than a thousand words.

```python
from bedrock.server import Server

app = Server()

@app.server_event
async def ready(ctx):
    print(f"Ready @ {ctx.host}:{ctx.port}!")

@app.game_event
async def block_broken(ctx):
    await ctx.server.run("title @a title Who destroyed {ctx.id}?!")

app.start("localhost", 6464)
```

*Please refer to the "Introduction" section in the documentation in
order to get started with bedrockpy.*

<!-- end brief-hook -->


## Installation

<!-- start installation-hook -->

You can install/upgrade *bedrockpy* with the following command:

```console
pip install -U bedrockpy
```

If you are not using Windows, you may as well enable
[uvloop](https://github.com/MagicStack/uvloop) which speeds up
the server:

```console
pip install -U "bedrockpy[fast]"
```

<!-- end installation-hook -->

---

NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH
MOJANG.
