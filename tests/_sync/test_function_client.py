import pytest
import respx
from httpx import Response
from jwt import encode

from supabase_functions.errors import FunctionsHttpError, FunctionsRelayError

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


def test_invoke():
    with respx.mock:
        route = respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(200)
        )
        function_client().invoke(function_name="hello-world")
        assert route.called


def test_invoke_with_json_response():
    with respx.mock:
        route = respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(200, json={"world": "Supabase"})
        )
        response = function_client().invoke(
            function_name="hello-world", invoke_options={"responseType": "json"}
        )
        assert route.called
        assert response == {"world": "Supabase"}


def test_invoke_with_relay_error():
    with respx.mock:
        respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(200, headers={"x-relay-header": "true"}),
            side_effect=FunctionsRelayError("Relay error!"),
        )
        with pytest.raises(FunctionsRelayError, match=r"Relay error!"):
            function_client().invoke(function_name="hello-world")


def test_invoke_with_non_200_response():
    with respx.mock:
        respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(404),
            side_effect=FunctionsHttpError("Http error!"),
        )
        with pytest.raises(FunctionsHttpError, match=r"Http error!") as exc:
            function_client().invoke(function_name="hello-world")
        assert exc.value.message == "Http error!"


def test_relay_error_message():
    with respx.mock:
        respx.post(f"{FUNCTIONS_URL}/hello-world").mock(
            return_value=Response(200, headers={"x-relay-header": "true"}),
            side_effect=FunctionsRelayError("Relay error!"),
        )
        with pytest.raises(FunctionsRelayError, match=r"Relay error!") as exc:
            function_client().invoke(function_name="hello-world")
        assert exc.value.message == "Relay error!"
