from httpx import HTTPError, Response
from typing import Any, Dict, Literal, Optional, Union

from ..errors import FunctionsHttpError, FunctionsRelayError

from ..utils import AsyncClient, __version__


class AsyncFunctionsClient:
    def __init__(self, url: str, headers: Dict):
        self.url = url
        self.headers = {
            "User-Agent": f"supabase-py/storage3 v{__version__}",
            **headers,
        }

    async def _request(
        self,
        method: Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"],
        url: str,
        headers: Union[Dict[str, str], None] = None,
        json: Optional[dict[Any, Any]] = None,
    ) -> Response:
        async with AsyncClient(base_url=self.url, headers=self.headers) as client:
            response = await client.request(method, url, json=json, headers=headers)
            try:
                response.raise_for_status()
            except HTTPError:
                raise Exception({**response.json(), "statusCode": response.status_code})

            return response

    def set_auth(self, token: str) -> None:
        """Updates the authorization header

        Parameters
        ----------
        token : str
            the new jwt token sent in the authorization header
        """

        self.headers["Authorization"] = f"Bearer {token}"

    async def invoke(self, function_name: str, invoke_options: Dict = {}) -> Dict:
        """Invokes a function

        Parameters
        ----------
        function_name : the name of the function to invoke
        invoke_options : object with the following properties
            `headers`: object representing the headers to send with the request
            `body`: the body of the request
            `responseType`: how the response should be parsed. The default is `json`

        Returns
        -------
        Dict
            Dictionary with data and/or error message
        """
        headers = {**self.headers, **invoke_options.get("headers", {})}
        body = invoke_options.get("body")
        if type(body) == str:
            headers["Content-Type"] = "text/plain"
        elif type(body) == dict:
            headers["Content-Type"] = "application/json"

        response_type = invoke_options.get("responseType")
        response = await self._request(
            "POST", f"{self.url}/{function_name}", headers=headers, json=body
        )
        is_relay_error = response.headers.get("x-relay-header")

        if is_relay_error and is_relay_error == "true":
            raise FunctionsRelayError(response.json().get("error"))

        if response.is_success is not True:
            raise FunctionsHttpError(response.json().get("error"))

        if response_type == "json":
            data = response.json()
        else:
            data = response.content
        return data
