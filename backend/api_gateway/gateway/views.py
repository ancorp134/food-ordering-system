import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .services import AUTH_SERVICE_URL,RESTAURANT_SERVICE_URL


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
    


class RestaurantProxy(APIView):

    permission_classes = [IsAuthenticated]

    def _forward_headers(self, request):
        headers = {
            "Content-Type": "application/json"
        }
        auth_header = request.headers.get("Authorization")
        print(auth_header)
        if auth_header:
            headers["Authorization"] = auth_header
        return headers
    
    def get(self,request):
        print("entering.......")
        url = f"{RESTAURANT_SERVICE_URL}/restaurants/"
        headers = self._forward_headers(request)
        respone = requests.get(url=url,headers=headers,timeout=5)
        try:
            data = respone.json()
        except ValueError:
            data = respone.text or None
        
        return Response(data,status=respone.status_code)

