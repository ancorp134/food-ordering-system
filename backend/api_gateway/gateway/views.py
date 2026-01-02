import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .services import AUTH_SERVICE_URL,RESTAURANT_SERVICE_URL,CART_SERVICE_URL
from api_gateway.Clients.order_client import *

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

    def get_permissions(self):
        if self.request.method == "GET":
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

    def get(self, request):
        url = f"{RESTAURANT_SERVICE_URL}/restaurants/"
        headers = self._forward_headers(request)

        response = requests.get(
            url=url,
            headers=headers,
            timeout=5
        )

        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)

    def post(self, request,path=""):
        url = f"{RESTAURANT_SERVICE_URL}/restaurants/{path}/"
        headers = self._forward_headers(request)

        response = requests.post(
            url=url,
            json=request.data,
            headers=headers,
            timeout=5
        )

        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)
    
class RestaurantCategoryProxy(APIView):

    permission_classes = [IsAuthenticated]

    def _forward_headers(self, request):
        headers = {
            "Content-Type": "application/json"
        }
        auth_header = request.headers.get("Authorization")
        if auth_header:
            headers["Authorization"] = auth_header

        return headers
    

    def post(self,request,path=""):
        url = f"{RESTAURANT_SERVICE_URL}/categories/{path}/"
        headers = self._forward_headers(request)

        response = requests.post(
            url=url,
            json = request.data,
            headers=headers,
            timeout=5
        )

        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)
    


class CartProxy(APIView):

    permission_classes =  [IsAuthenticated]

    def _forward_headers(self, request):
        headers = {
            "Content-Type": "application/json"
        }
        auth_header = request.headers.get("Authorization")
        if auth_header:
            headers["Authorization"] = auth_header

        return headers
    
    def get(self,request):
        url = f"{CART_SERVICE_URL}/cart/"
        headers =self._forward_headers(request)

        response = requests.get(url=url,headers=headers,timeout=5)
        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)
    
    def delete(self,request):
        url = f"{CART_SERVICE_URL}/cart/"
        headers =self._forward_headers(request)

        response = requests.get(url=url,headers=headers,timeout=5)
        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)
    
    def post(self,request):
        url = f"{CART_SERVICE_URL}/cart/items/"
        headers = self._forward_headers(request)

        response = requests.post(
            url=url,
            json = request.data,
            headers=headers,
            timeout=5
        )

        try:
            data = response.json()
        except ValueError:
            data = response.text or None

        return Response(data, status=response.status_code)
    

    def patch(self,request,item_id):
        url = f"{CART_SERVICE_URL}/cart/items/{item_id}/"
        headers = self._forward_headers(request)

        response = requests.patch(
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
    
    def delete(self,request,item_id):
        url = f"{CART_SERVICE_URL}/cart/items/{item_id}/"
        headers = self._forward_headers(request)

        response = requests.delete(
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



    

class OrderCheckoutProxy(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):

        client = OrderServiceClient(
            request.headers.get("Authorization")
        )
        response = client.checkout(request.data)
        return Response(response.json(),status=response.status_code)
    

    def get(self,request):
        client = OrderServiceClient(
            request.headers.get("Authorization")
        )
        response = client.myorders()
        return Response(response.json(),status=response.status_code)

    

        



