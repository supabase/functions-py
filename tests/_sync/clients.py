from jwt import encode

from supabase_functions import SyncFunctionsClient

GOTRUE_JWT_SECRET = "37c304f8-51aa-419a-a1af-06154e63707a"
FUNCTIONS_URL = "http://localhost:54321/functions/v1"


def mock_access_token() -> str:
    return encode(
        {
            "sub": "1234567890",
            "role": "anon_key",
        },
        GOTRUE_JWT_SECRET,
    )


def function_client():
    return SyncFunctionsClient(
        url=FUNCTIONS_URL,
        headers={
            "apiKey": mock_access_token(),
            "Authorization": f"Bearer {mock_access_token()}",
        },
        timeout = 10
    )
