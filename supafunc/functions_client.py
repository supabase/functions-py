import httpx
from typing import Dict


class FunctionsClient:
    def __init__(self, url: str, headers: Dict):
        self.url = url
        self.headers = headers

    def set_auth(self, token: str) -> None:
        """Updates the authorization header

        Parameters
        ----------
        token : str
            the new jwt token sent in the authorization header
        """

        self.headers["Authorization"] = f"Bearer {token}"

    async def invoke(self, function_name: str, invoke_options: Dict) -> Dict:
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
        try:
            headers = {**self.headers, **invoke_options.get('headers', {})}
            body = invoke_options.get('body')
            response_type = invoke_options.get('responseType')
            response = httpx.post(
                f"{self.url}/{function_name}", headers=headers, json=body)
            is_relay_error = response.headers.get('x-relay-header')
            if is_relay_error and is_relay_error == 'true':
                return {
                    "data": None,
                    "error": response.text
                }
            if response_type == 'json':
                data = response.json()
            else:
                data = response.content
            return {"data": data, "error": None}
        except Exception as e:
            return {
                "data": None,
                "error": e
            }
