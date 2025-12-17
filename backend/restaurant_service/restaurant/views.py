from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RestaurantListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(Self,request):
        user = request.user
        if user.role.lower() == "customer":
            query_set = Restaurant.objects.all()
        elif user.role.lower() == "restaurant_owner":
            query_set = Restaurant.objects.filter(owner_id = user.id)
        else:
            pass

        serializer = RestaurantSerializer(query_set,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        user = request.user

        if user.role.lower() != "restaurant_owner" :
            return  Response({"message" : "Access Denied"},status=status.HTTP_200_OK)
        else:
            pass

        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_Valid():
            serializer.save(owner_id=user.id)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
