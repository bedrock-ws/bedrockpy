# Troubleshooting

Some errors might occur while trying to start the server or connect
to it. This section covers how to fix common issues.

Is there an error you do not know how to fix? Consider
[opening an issue on GitHub}(https://github.com/bedrock-ws/bedrockpy/issues/new/choose)!
We and others are glad to help you.


## "Address already in use"

The port you have chosen is already used by another program. Try out
another 4-digit value. "6464" is used in all examples in the documentation.

Example:

```python
# change this:
app.start("localhost", 6464)

# to this:
app.start("localhost", 7654)
```


## "Could not connect to server: ..."

Mke sure you have disabled "Require Encrypted Websockets" when you do not
use an encrypted connection (which is usually the case). Sometimes you
might have to type the `/connect` or `/wsserver` over and over or restart
the server by stopping the program and running it again.
