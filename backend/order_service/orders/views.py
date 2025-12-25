from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.



class OrderCheckOut(APIView):

    permission_classes =  [IsAuthenticated]

    def post(self,request):
        serializer = OrderSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

