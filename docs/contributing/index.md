# Contributing

{{wip}}

```{attention}
Throughout the source code the term "command" usually refers to data sent
to the client and not a Minecraft command. These terms are used interchangeably.
```

```{toctree}
---
titlesonly: true
---
writing
translating
```


## Installation

There are some extra dependencies that need to be installed for
development.

First, [install Poetry](https://python-poetry.org/docs/#installation).

{{wip}}

```bash
git clone https://github.com/bedrock-ws/bedrockpy.git && cd $_
```

```console
poetry install --with docs
```


## Run Examples

```console
poetry run python examples/eggs.py
```


## Run checks and tests

```console
tox run
```


