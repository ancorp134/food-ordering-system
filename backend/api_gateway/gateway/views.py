import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .services import AUTH_SERVICE_URL


class AuthProxy(APIView):

    def get_permissions(self):
        if self.kwargs.get("path") in ["login", "register"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    def post(self, request, path):
        url = f"{AUTH_SERVICE_URL}/auth/{path}/"

        headers = {
            "Content-Type": "application/json"
        }

        auth_header = request.headers.get("Authorization")
        if auth_header:
            headers["Authorization"] = auth_header

        print(headers["Authorization"])
        
        response = requests.post(
            url,
            json=request.data,
            headers=headers,
            timeout=5
        )

        # 🔥 SAFE RESPONSE HANDLING
        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)
