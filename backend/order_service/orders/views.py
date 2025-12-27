from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Order
# Create your views here.


class OrderCheckOut(APIView):

    permission_classes = [IsAuthenticated]


    

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
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
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)