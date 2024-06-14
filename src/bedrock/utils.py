from __future__ import annotations

from collections.abc import Iterable, Mapping
from enum import Enum
import json
from typing import Literal, NewType

from attrs import define


def rawtext(
    text: str
    | Iterable[
        Mapping[Literal["text", "selector", "translate"], str]
        | Mapping[Literal["score"], Mapping[Literal["name", "objective"], str]]
    ]
) -> str:
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
        '{"rawtext": [{"text": "Hello World"}]}'
        >>> rawtext([{'text': 'Hello '}, {'selector': '@p[r=10]'}])
        '{"rawtext": [{"text": "Hello "}, {"selectors": "@p[r=10]}]}'

    """
    if isinstance(text, str):
        return json.dumps({"rawtext": [{"text": text}]})
    else:
        return json.dumps({"rawtext": text})


class TargetSelector(str, Enum):
    """
    A collection of target selectors that can be used within commands.

    .. seealso:: https://minecraft.wiki/w/Target_selectors
    """

    NEAREST_PLAYER = "@p"
    RANDOM_PLAYER = "@r"
    ALL_PLAYERS = "@a"
    ALL_ENTITIES = "@e"
    SELF = "@s"
    PLAYER_AGENT = "@c"
    ALL_AGENTS = "@v"
    INITIATOR = "@initiator"


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
        """Parses a world coordinate.

        Parameters
        ----------
        value
            The coordinate to parse.

        Examples
        --------
        .. code-block:: python

            from bedrock.utils import WorldCoordinate, WorldCoordinates

            x = WorldCoordinate.from_string("17")
            y = WorldCoordinate.from_string("~27")
            z = WorldCoordinate.from_string("~-27.4928")

            goto = WorldCoordinates((x, y, z))
        """
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
        """Parses a local coordinate.

        Parameters
        ----------
        value
            The coordinate to parse.

        Examples
        --------
        .. code-block:: python

            from bedrock.utils import LocalCoordinate, LocalCoordinates

            x = LocalCoordinate.from_string("^1")
            y = LocalCoordinate.from_string("^-19.5752")
            z = LocalCoordinate.from_string("^0")

            goto = LocalCoordinates((x, y, z))
        """
        n = value.removeprefix("^")
        if len(n) != len(value):
            raise ValueError("local coordinate must start with a caret (^)")
        return cls(numeric(n))


WorldCoordinates = NewType(
    "WorldCoordinates", tuple[WorldCoordinate, WorldCoordinate, WorldCoordinate]
)
LocalCoordinates = NewType(
    "LocalCoordinates", tuple[LocalCoordinate, LocalCoordinate, LocalCoordinate]
)


def boolean(value: str) -> bool:
    """Converts a string into a boolean.

    Parameters
    ----------
    value
        The string to convert into a boolean.

        * ``'y'``/``'yes'``/``'true'`` \N{RIGHTWARDS DOUBLE ARROW} ``True``
        * ``'n'``/``'no'``/``'false'`` \N{RIGHTWARDS DOUBLE ARROW} ``False``

        .. note::

            The string is converted into lower case before comparing. That means
            that ``'TRUe'`` results in ``True`` as well.

    Examples
    --------
    .. code-block:: python

        >>> from bedrock.utils import boolean
        >>> boolean("y")
        True
        >>> boolean("yes")
        True
        >>> boolean("true")
        True
        >>> boolean("trUE")
        True
        >>> boolean("1")
        Traceback (most recent call last):
          File "<stdin>", line 1 in <module>
        ValueError: cannot turn '1' into a boolean
        >>> boolean("n")
        False
        >>> boolean("NO")
        False
        >>> boolean("False")
        False
        >>>

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

    The major reason to use this instead of :external+python:class:`float`
    is for usage within game commands such as ``teleport`` where an integer
    coordinate like ``42`` is parsed as ``42.50`` whereas floating points
    are interpreted as is so that ``21.0`` means ``21.0``. You may override
    this behaviour by overriding this function which affects the parsing of
    :meth:`WorldCoordinate.from_string` and :meth:`LocalCoordinate.from_string`:

    .. code-block:: python

        from bedrock import utils
        utils.numeric = float

    Parameters
    ----------
    value
        The string to converr into a numeric.

    Examples
    --------
    .. code-block:: python

        >>> from bedrock.utils import numeric
        >>> numeric("10")
        10
        >>> numeric("10.500")
        10.5
        >>>

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
