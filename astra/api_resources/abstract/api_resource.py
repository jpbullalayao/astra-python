from astra.api_requestor import APIRequestor


class APIResource(object):
    RESOURCE_NAME = ""

    @classmethod
    def class_url(cls):
        base = cls.RESOURCE_NAME
        return f'{base}s'

    def request(self):
        pass

    @classmethod
    def static_request(cls, http_method, url, params):
        requestor = APIRequestor()

        response = requestor.request(http_method, url, params)
        return response

