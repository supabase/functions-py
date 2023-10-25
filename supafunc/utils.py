from httpx import AsyncClient as AsyncClient  # noqa: F401
from httpx import Client as BaseClient

__version__ = "0.2.4"


class SyncClient(BaseClient):
    def aclose(self) -> None:
        self.close()
