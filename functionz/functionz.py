from typing import Dict
import httpx


class FunctionsClient:
    def __init__(self, url: str, headers: Dict):
        self.url = url
        self.headers = headers

    async def invoke(self, function_name: str, invoke_options: Dict):
        try:
            headers = invoke_options.get('headers')
            body = invoke_options.get('body')
            response = await httpx.post(f"{self.url}/{function_name}", headers=headers)
            is_relay_error = response.headers.get('x-relay-header')
            if is_relay_error and is_relay_error == 'true':
                return {
                    "data": None,
                    "error": response.tex
                }
            # TODO: Convert type accordingly

            return {"data": response.data, "error": None}
        except Exception as e:
            return {
                "data": None,
                "error": e
            }
