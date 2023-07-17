from __future__ import annotations

from attrs import define


@define
class CommandRequestError(Exception):
    _message: str
    _status: int

    def __str__(self) -> str:
        return self._message
