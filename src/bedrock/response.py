from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from attrs import define

from .exceptions import CommandRequestError


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

    @property
    def ok(self) -> bool:
        """Returns ``True`` when the command has been executed successfully."""
        return self.status == 0

    @classmethod
    def parse(cls, data: Mapping[str, Any]) -> CommandResponse:
        """Parses a JSON object sent by the client."""
        return cls(
            message=data["body"].get("statusMessage"),
            status=data["body"]["statusCode"],
        )

    def raise_for_status(self) -> None:
        """
        Raises :class:`bedrock.exceptions.CommandRequestError` if the command did
        not run successfully. Otherwise this method returns ``None``.
        """
        if not self.ok:
            raise CommandRequestError(self.message, self.status)
