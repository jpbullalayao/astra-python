import astra
import requests

from requests.auth import HTTPBasicAuth

from astra.astra_response import AstraResponse
from astra.error import AuthenticationError, APIError


class APIRequestor(object):
    def __init__(
        self,
        api_token=None,
        api_base=None,
    ):
        self.api_token = api_token or astra.api_token
        self.api_base = api_base or astra.api_base

    def request(self, http_method, url, params=None, headers=None):
        if self.api_token is None:
            raise AuthenticationError(
                "No API token provided. (HINT: set your API token using "
                '"astra.api_token = <API-TOKEN>").'
            )

        abs_url = f"{self.api_base}{url}"
        headers = self.request_headers()

        method_to_use = getattr(requests, http_method.lower())
        basic = HTTPBasicAuth('d1be1c20205a4f08b92b8cee416c01a0', self.api_token)
        print(basic)
        # rbody = method_to_use(abs_url, json=params, headers=headers, auth=basic)
        rbody = method_to_use(abs_url, json=params, headers=headers, auth=basic)
        print(rbody.json())
        return self.interpret_response(rbody)
 
    def request_headers(self):
        headers = {
            "Authorization": f'Bearer {self.api_token}',
            "accept": "application/json",
            "content-type": "application/json"
        }
        return headers

    def interpret_response(self, rbody):
        try:
            resp = AstraResponse(rbody)
        except Exception:
            raise APIError(
                f'Invalid response body from API: {rbody}'
            )
        return resp
