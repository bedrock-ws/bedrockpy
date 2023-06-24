# Setup

## Configure settings in the game

```{video} _static/settings.mp4
---
alt: Settings → General → Require Encrypted Websockets → Disable
autoplay: true
loop: true
muted: true
---
```

Settings → General → Require Encrypted Websockets → Disable


## Testing

Instead of writing an entire server just to ensure
everything is set up correctly, *bedrockpy* provides a simple script
we can run to find this out with one simple command.

```console
python -m bedrock._demo
```

Follow the instructions shown on the terminal. After you have successfully
connected the server should send a message in the game saying "Yeah! It works."

```{note}
If the above does not work correctly, check out the
[troubleshooting page](./troubleshooting.md).
```

Congratulations, you have successfully established a connection and can
proceed writing your own server. You will learn how to do that on the next page.
