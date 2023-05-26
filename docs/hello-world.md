# *Hello World* with *bedrockpy*

Now, we are finally ready to write some code! Let's start with a simple
example.

```python
from bedrock.server import Server

app = Server()

app.start("localhost", 6464)
```

````{tip}
If the device running the server should not be the same running the
game, the private IP address of your device is required instead of
"localhost"/`127.0.0.1`. The device connecting to the server needs
to be in the same network as the device running the server.

The private IP adress usually starts with "192" and can be retrieved
easily by using this command in the terminal:

```console
python -c "from bedrock._demo import get_ip; print(get_ip())"
```

If you choose to use the private IP instead of "localhost"/`127.0.0.1`,
the `/connect` command should use that private IP address as well instead
of "localhost"/`127.0.0.1`. For example:

```text
/connect 192.168.69.420
```

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
