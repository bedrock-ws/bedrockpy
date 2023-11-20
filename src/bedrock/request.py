import asyncio
from collections.abc import Mapping
from uuid import UUID
from typing import Any

from attrs import define

from .response import CommandResponse


@define
class CommandRequest:
    """A command request sent to the server."""

    _identifier: UUID
    _data: Mapping[str, Any]
    _response: asyncio.Future[CommandResponse]

    @property
    def identifier(self) -> UUID:
        """The unique id of the request."""
        return self._identifier

    @property
    def data(self) -> Mapping[str, Any]:
        """The data of the request."""
        return self._data

    @property
    def response(self) -> asyncio.Future[CommandResponse]:
        """The response of the response wrapped inside a :external+python:class:`asyncio.Future`."""
        return self._response
