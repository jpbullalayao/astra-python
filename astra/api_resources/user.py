from astra.api_resources.abstract.api_resource import APIResource

class User(APIResource):
    @classmethod
    def create_user_intent(cls, params):
        return cls.static_request('post', 'user_intent', params)
