import json

class AstraResponse(object):
    def __init__(self, body):
        self.body = body
        self.data = json.loads(body)
