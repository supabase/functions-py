import pytest
import respx
from httpx import Response
from jwt import encode

from supafunc.errors import FunctionsHttpError, FunctionsRelayError

from .clients import (
    FUNCTIONS_URL,
    GOTRUE_JWT_SECRET,
    function_client,
    mock_access_token,
)


def test_auth_header():
    client = function_client()
    assert client.headers.get("Authorization") == f"Bearer {mock_access_token()}"


def test_set_auth():
    auth_token = encode(
        {
            "sub": "9876543210",
            "role": "my_anon_key",
        },
        GOTRUE_JWT_SECRET,
    )
    client = function_client()
    client.set_auth(token=auth_token)
    assert client.headers.get("Authorization") == f"Bearer {auth_token}"


async def test_invoke():
    async with respx.mock:
        route = respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(200)
        )
        await function_client().invoke(function_name="hello-world")
        assert route.called


async def test_invoke_with_json_response():
    async with respx.mock:
        route = respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(200, json={"world": "Supabase"})
        )
        response = await function_client().invoke(
            function_name="hello-world", invoke_options={"responseType": "json"}
        )
        assert route.called
        assert response == {"world": "Supabase"}


async def test_invoke_with_relay_error():
    async with respx.mock:
        respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(200, headers={"x-relay-header": "true"}),
            side_effect=FunctionsRelayError("Relay error!"),
        )
        with pytest.raises(FunctionsRelayError, match=r"Relay error!"):
            await function_client().invoke(function_name="hello-world")


async def test_invoke_with_non_200_response():
    async with respx.mock:
        respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(404),
            side_effect=FunctionsHttpError("Http error!"),
        )
        with pytest.raises(FunctionsHttpError, match=r"Http error!"):
            await function_client().invoke(function_name="hello-world")
