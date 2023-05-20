# Hello World with *bedrockpy*

Now, we are finally ready to write some code! Let's start with a simple
example.

```python
from bedrock.server import Server

app = Server()

app.start("localhost", 6464)
```

````{tip}
If the server running the server is not the same running the game, the IP
address of your device is required instead of "localhost". The device
connecting to the server needs to be in the same network as the server.

The IP adress should start with "192" and can be retrieved easily by
using this command:

```console
python -c "from bedrock._demo import get_ip; print(get_ip())"
```

If you choose to go with the IP instead of "localhost" the `/connect`
command must include the IP as well instead of "localhost".
````

First, we import the {py:class}`bedrock.server.Server` class from the
module {py:mod}`bedrock.server` in the {py:mod}`bedrock`
(**not** "bedrockpy") package.

{{wip}}

## Establish Connection

As metioned earlier, a connection to the server can be established by
typing `/connect localhost:6464`

## Close Connection

From the server side it is poosible to close the server and therefore
closing the connection by simply using {kbd}`CTRL+C` in the terminal.

The player who established the connection may type `/connect x` in the
chat where `x` may be any text. Alternatively, the connection is also
closed when the player closes the game.
