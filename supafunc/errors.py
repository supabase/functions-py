from __future__ import annotations

from typing_extensions import TypedDict


class FunctionsError(Exception):
    def __init__(self, message: str) -> None:
        Exception.__init__(self, message)
        self.message = message
        self.name = "FunctionsError"


class FunctionsApiErrorDict(TypedDict):
    name: str
    message: str
    status: int


class CustomFunctionsError(FunctionsError):
    def __init__(self, message: str, name: str, status: int) -> None:
        FunctionsError.__init__(self, message)
        self.name = name
        self.status = status

    def to_dict(self) -> FunctionsApiErrorDict:
        return {
            "name": self.name,
            "message": self.message,
            "status": self.status,
        }


class FunctionsHttpError(CustomFunctionsError):
    def __init__(self, message: str) -> None:
        super().__init__(
            self,
            message,
            "FunctionsHttpError",
            400,
        )


class FunctionsRelayError(CustomFunctionsError):
    """Base exception for relay errors."""

    def __init__(self, message: str) -> None:
        super().__init__(
            self,
            message,
            "FunctionsHttpError",
            400,
        )
