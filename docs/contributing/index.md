# Contributing

## In what ways can I contribute?

<!-- Maybe move this part into a CODE_OF_CONDUCT.md file and `include` it in the future -->

We welcome any kind of contributions - let it be just a reference to a typo.

Here are a few examples of ways you can contribute:


- Mention issue in documentation (e.g. grammar, typos, UI)
- Writing blogs which are included in the documentation
- Translating
- Fixing bugs
- Sharing feature request

To avoid repeating ourselves and make your way faster and transparent we aks you to
read this section carefully. But don't worry, if you don't understand something or
want to make sure you don't make something wrong, then you can ask us.


## Notes

Throughout the source code the term "command" usually refers to data sent
to the client and not a Minecraft command. These terms are used interchangeably.


## Installation

There are some extra dependencies that need to be installed for
development. This only affects you if you consider working on the
codebase (including documentation).

First, [install Poetry](https://python-poetry.org/docs/#installation).

{{wip}}

```bash
git clone https://github.com/bedrock-ws/bedrockpy.git
cd bedrockpy
```

```console
poetry install --all-extras
```


## View Documentation

```bash
# from the root directory
cd docs
poetry run make html
poetry run python -m http.server -d _build/html
```

## Run Tests

```console
tox run
```


## Submitting Pull Requests

### Commits

Consider commiting each small change.

Commit messages should be precise and clear and should have the following form:

- Start with an emoji.
- Followed by one space.
- First character of first word is in uppercase.
- Present tense.

Example:

```bash
git commit -m "ℹ️ Add email to authors"
```

Here is some inspiration for the emojis:

Emoji | Meaning
------|--------
🔨    | Fix
🗑️    | Removal
➕    | Addition
🔠    | Changes on text
📖    | Changes on documentation
✨    | Changes on style


### Pushing

Provide an exact description of your changes.

{{ wip }}


## Table of Contents

```{toctree}
---
titlesonly: true
---
writing
translating
```
