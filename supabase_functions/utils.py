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
