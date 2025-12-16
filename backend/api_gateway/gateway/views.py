import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .services import AUTH_SERVICE_URL


class AuthProxy(APIView):

    def get_permissions(self):
        if self.kwargs.get("path") in ["login", "register"]:
            print(self.kwargs.get("path"))
            return [AllowAny()]
        return [IsAuthenticated()]

    def _forward_headers(self, request):
        headers = {
            "Content-Type": "application/json"
        }
        auth_header = request.headers.get("Authorization")
        if auth_header:
            headers["Authorization"] = auth_header
        return headers

    def post(self, request, path):
        print(path)
        url = f"{AUTH_SERVICE_URL}/auth/{path}/"
        headers = self._forward_headers(request)

        print("POST Authorization:", headers.get("Authorization"))

        response = requests.post(
            url,
            json=request.data,
            headers=headers,
            timeout=5
        )

        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)

    def get(self, request, path):
        print(path)
        url = f"{AUTH_SERVICE_URL}/auth/{path}/"
        headers = self._forward_headers(request)

        print("GET Authorization:", headers.get("Authorization"))

        response = requests.get(
            url,
            headers=headers,
            timeout=5
        )

        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)
