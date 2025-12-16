from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from gateway.user import GatewayUser


class GatewayJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None

        try:
            prefix, token = auth_header.split()
            if prefix.lower() != "bearer":
                raise AuthenticationFailed("Invalid token prefix")
        except ValueError:
            raise AuthenticationFailed("Invalid Authorization header")

        try:
            validated_token = AccessToken(token)
        except Exception:
            raise AuthenticationFailed("Invalid or expired token")

        # 🔥 Create authenticated gateway user
        user = GatewayUser(validated_token.payload)

        return (user, validated_token)
