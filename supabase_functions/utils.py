from urllib.parse import urlparse

from httpx import AsyncClient as AsyncClient  # noqa: F401
from httpx import Client as BaseClient

DEFAULT_FUNCTION_CLIENT_TIMEOUT = 5


class SyncClient(BaseClient):
    def aclose(self) -> None:
        self.close()


def is_valid_str_arg(target: str) -> bool:
    return isinstance(target, str) and len(target.strip()) > 0


def is_http_url(url: str) -> bool:
    return urlparse(url).scheme in {"https", "http"}


def is_valid_jwt(value: str) -> bool:
    """Checks if value looks like a JWT, does not do any extra parsing."""
    if not isinstance(value, str):
        return False

    # Remove trailing whitespaces if any.
    value = value.strip()

    # Remove "Bearer " prefix if any.
    if value.startswith("Bearer "):
        value = value[7:]

    # Valid JWT must have 2 dots (Header.Paylod.Signature)
    if value.count(".") != 2:
        return False

    okcr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-."
    for char in value:
        if not char in okcr:
            return False

    return True
