# Contributing

{{wip}}

```{toctree}
---
titlesonly: true
---
writing
translating
```


## Notes

Throughout the source code the term "command" usually refers to data sent
to the client and not a Minecraft command. These terms are used interchangeably.


## Installation

There are some extra dependencies that need to be installed for
development.

First, [install Poetry](https://python-poetry.org/docs/#installation).

{{wip}}

```bash
git clone https://github.com/bedrock-ws/bedrockpy.git && cd $_
```

```console
poetry install --all-extras
```


## View Documentation

```console
cd docs
poetry run make html
poetry run python -m http.server -d _build/html
```

## Run Tests

```console
tox run
```


