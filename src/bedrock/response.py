from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from attrs import define


def parse(data: Mapping[str, Any]) -> CommandResponse | CommandResponseError:
    """Parses a JSON object sent by the client."""
    message = data["body"].get("statusMessage")
    status=data["body"]["statusCode"]

    res = CommandResponse(message, status)
    if not res.ok():
        return CommandResponseError(message, status)
    return res

@define
class CommandResponse:
    """A response sent by the client."""

    _message: str
    _status: int

    @property
    def message(self) -> str:
        """The message of the response."""
        return self._message
    
    @property
    def status(self) -> int:
        """The status of the response."""
        return self._status

    @classmethod
    def parse(cls, data: Mapping[str, Any]) -> CommandResponse:
        """Parses a JSON object sent by the client."""
        return cls(
            message=data["body"].get("statusMessage"),
            status=data["body"]["statusCode"],
        )

    def ok(self) -> bool:
        """Returns ``True`` when the command has been executed successfully."""
        return self.status == 0

@define
class CommandResponseError(Exception):
    """A response sent by the client that indicates an error."""

    _message: str
    _status: int

    @property
    def message(self) -> str:
        """The message of the response."""
        return self._message
    
    @property
    def status(self) -> int:
        """The status of the response."""
        return self._status

    @classmethod
    def parse(cls, data: Mapping[str, Any]) -> CommandResponseError:
        """Parses a JSON object sent by the client."""
        return cls(
            message=data["body"].get("statusMessage"),
            status=data["body"]["statusCode"],
        )
