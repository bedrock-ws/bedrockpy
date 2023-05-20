from __future__ import annotations

from enum import Enum
import json
from typing import Iterable, Literal, Mapping, NewType

from attrs import define


def rawtext(text: str | Iterable[
    Mapping[
        Literal["text"] | Literal["selector"],
        str
    ] | Mapping[
        Literal["score"],
        Mapping[
            Literal["name"] | Literal["objective"],
            str
        ]
    ]]) -> str:
    """
    Wraps text inside a rawtext JSON object which can be used for
    ``/tellraw``, ``/titleraw`` etc.
    
    .. seealso:: https://wiki.bedrock.dev/commands/tellraw.html

    Parameters
    ----------
    text
        Either just a string or an iterable of mappings beeing
        valid rawtext parts.

    Examples
    --------

    .. code-block:: python

        >>> from bedrock.utils import rawtext
        >>> rawtext('Hello World')
        '{"rawtext": [{"text": "Hello, World"}]}'
        >>> rawtext([{'text': 'Hello '}, {'selector': '@p[r=10]'}])
        '{"rawtext": [{"text": "Hello "}, {"selectors": "@p[r=10]}]}'
    
    """
    if isinstance(text, str):
        return json.dumps({
            "rawtext": [{"text": text}]
        })
    else:
        return json.dumps({
            "rawtext": text
        })


class TargetSelector(str, Enum):
    """
    A collection of target selectors that can be used within commands.
    
    .. seealso:: https://minecraft.fandom.com/wiki/Target_selectors
    """

    NEAREST_PLAYER = "@p"
    RANDOM_PLAYER  = "@r"
    ALL_PLAYERS    = "@a"
    ALL_ENTITIES   = "@e"
    SELF           = "@s"
    PLAYER_AGENT   = "@c"
    ALL_AGENTS     = "@v"
    INITIATOR      = "@initiator"

@define
class WorldCoordinate:
    """
    A class representing a world coordinate.
    """
    coord: float
    is_relative: bool = False

    def __str__(self) -> str:
        return f"{'~' if self.is_relative else ''}{self.coord}"

    @classmethod
    def from_string(cls, value: str) -> WorldCoordinate:
        n = value.removeprefix("~")
        return cls(numeric(n), is_relative=len(n) != len(value))


@define
class LocalCoordinate:
    """
    A class representing a local coordinate.
    """
    coord: float

    def __str__(self) -> str:
        return f"^{self.coord}"

    @classmethod
    def from_string(cls, value: str) -> LocalCoordinate:
        n = value.removeprefix("^")
        if len(n) != len(value):
            raise ValueError("local coordinate must start with a caret (^)")
        return cls(numeric(n))


WorldCoordinates = NewType(
    "WorldCoordinates",
    tuple[WorldCoordinate, WorldCoordinate, WorldCoordinate]
)
LocalCoordinates = NewType(
    "LocalCoordinates",
    tuple[LocalCoordinate, LocalCoordinate, LocalCoordinate]
)


def boolean(value: str) -> bool:
    """Converts a string into a boolean.
    
    Parameters
    ----------
    value
        The string to convert into a boolean.

        * ``'y'``/``'yes'``/``'true'`` \N{RIGHTWARDS DOUBLE ARROW} ``True``
        * ``'n'``/``'no'``/``'false'`` \N{RIGHTWARDS DOUBLE ARROW} ``False``

        *The string is converted into lower case before comparing.*

    Raises
    ------
    ValueError
        The string cannot be converted into a boolean.
    """
    if value.lower() in {"y", "yes", "true"}:
        return True
    elif value.lower() in {"n", "no", "false"}:
        return False
    raise ValueError(f"cannot turn {value!r} into a boolean")

def numeric(value: str) -> float:
    """
    Converts a string into an integer or if that fails into a floating
    point.

    Parameters
    ----------
    value
        The string to converr into a numeric.

    Raises
    ------
    ValueError
        The string cannot be converted into a boolean.
    """
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError as e:
            raise e from None
