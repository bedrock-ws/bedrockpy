<p align="center">
  <img
    src="https://github.com/bedrock-ws/bedrockpy/blob/main/bedrockpy_3d.png?raw=true"
    width="140vh"
  >
  <h1 align="center">bedrockpy</h1>
  <p align="center">
    Minecraft: Bedrock Edition Websocket Server
  </p>
</p>

<!-- start brief-hook -->

*bedrockpy* lässt Sie einen Websocket Server erstellen, welcher in der
Lage ist, mit einem Spieler in Minecraft zu interagieren. Wie der Name
bereits andeutet, funktioniert dieses Projekt nur mit der "Minecraft:
Bedrock Edition".

[![Dokumentation Status](https://readthedocs.org/projects/bedrockpy/badge/?version=latest&style=flat-square)](https://bedrockpy.readthedocs.io/en/latest/?badge=latest)
[![Lizenz](https://img.shields.io/github/license/bedrock-ws/bedrockpy?style=flat-square)](https://github.com/bedrock-ws/bedrockpy/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/bedrockpy?style=flat-square)](https://pypi.org/project/bedrockpy)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/bedrockpy?style=flat-square)](https://pypi.org/project/bedrockpy)


## Quick Links

- 📦 [PyPI](https://pypi.org/project/bedrockpy)
- 📖 [Doku](https://bedrockpy.readthedocs.io/)
- 🐍 [Repo](https://github.com/bedrock-ws/bedrockpy/)


## "Zeig mir etwas Code"

> Code sagt mehr als tausend Worte.

```python
from bedrock.server import Server

app = Server()

@app.server_event
async def ready(ctx):
    print(f"Bereit @ {ctx.host}:{ctx.port}!")

@app.game_event
async def block_broken(ctx):
    await ctx.server.run(f"title @a title Wer hat {ctx.id} zerstört?!")

app.start("localhost", 6464)
```

*Bitte lesen Sie die Sektion "Introduction", um mit bedeockpy zu starten.*


## Vorraussetzungen

- [Python](https://www.python.org) 3.10 oder höher
- [pip](https://pip.pypa.io/en/stable/) (kommt in der Regel mit Python)
- [Minecraft](https://www.minecraft.net/en-us) (**nicht** Java Edition) (jede Version)[^1]

[^1]: Nur dem Client, welcher die Verbindung mit dem Server eingeht betreffend.

<!-- end brief-hook -->


## Installation

<!-- start installation-hook -->

Sie können *bedrockpy* mit dem folgenden Befehl installieren/upgraden:

```console
pip install -U bedrockpy
```

Wenn Sie nicht Windows nutzen, können sie ebenfalls
[uvloop](https://github.com/MagicStack/uvloop) nutzen, was
die Geschwindigkeit des Servers beschleunigt:

```console
pip install -U "bedrockpy[fast]"
```

<!-- end installation-hook -->

---

NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH
MOJANG.

KEIN OFFIZIELLES MINECRAFT PRODUKT. NICHT VON MOJANG GENEHMIGT ODER MIT MOJANG ASSOZIIERT.
