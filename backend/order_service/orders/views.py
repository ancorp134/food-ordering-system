from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Order
from .cart_client import get_cart,clear_cart
# Create your views here.


class OrderCheckOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        auth_header = request.headers.get("Authorization")

        cart = get_cart(auth_header)

        if not cart or not cart.get("items"):
            return Response(
                {"detail": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST
            )

        
        order_payload = {
            "restaurant_id": cart["restaurant_id"],
            "items": cart["items"]
        }

        serializer = OrderSerializer(data=order_payload, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            clear_cart(auth_header)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerOrderView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        cust_id = request.user.token.get("user_id")

        try:
            orders = Order.objects.filter(customer_id = cust_id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = OrderSerializer(orders,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)