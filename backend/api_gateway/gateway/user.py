

class GatewayUser:
    def __init__(self, token_payload):
        self.token_payload = token_payload
        self.is_authenticated = True

    @property
    def id(self):
        return self.token_payload.get("user_id")

    @property
    def role(self):
        return self.token_payload.get("role")
