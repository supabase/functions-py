from httpx import AsyncClient as AsyncClient  # noqa: F401
from httpx import Client as BaseClient

DEFAULT_FUNCTION_CLIENT_TIMEOUT = 5


class SyncClient(BaseClient):
    def aclose(self) -> None:
        self.close()
