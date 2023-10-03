class AstraError(Exception):
    def __init__(
        self,
        message=None
    ):
        super(AstraError, self).__init__(message)


class APIError(AstraError):
    pass

class AuthenticationError(AstraError):
    pass

