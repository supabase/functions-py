import re
import sys
from urllib.parse import urlparse

from httpx import AsyncClient as AsyncClient  # noqa: F401
from httpx import Client as BaseClient

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from strenum import StrEnum


DEFAULT_FUNCTION_CLIENT_TIMEOUT = 5
BASE64URL_REGEX = r"^([a-z0-9_-]{4})*($|[a-z0-9_-]{3}$|[a-z0-9_-]{2}$)$"


class FunctionRegion(StrEnum):
    Any = "any"
    ApNortheast1 = "ap-northeast-1"
    ApNortheast2 = "ap-northeast-2"
    ApSouth1 = "ap-south-1"
    ApSoutheast1 = "ap-southeast-1"
    ApSoutheast2 = "ap-southeast-2"
    CaCentral1 = "ca-central-1"
    EuCentral1 = "eu-central-1"
    EuWest1 = "eu-west-1"
    EuWest2 = "eu-west-2"
    EuWest3 = "eu-west-3"
    SaEast1 = "sa-east-1"
    UsEast1 = "us-east-1"
    UsWest1 = "us-west-1"
    UsWest2 = "us-west-2"


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

    for part in value.split("."):
        if not re.search(BASE64URL_REGEX, part, re.IGNORECASE):
            return False

    return True
