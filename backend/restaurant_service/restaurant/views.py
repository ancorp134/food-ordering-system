from django.urls import path
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from restaurant.models import Restaurant,MenuItem,Category
from restaurant.serializers import RestaurantSerializer,CategorySerializer,MenuItemSerializer


class RestaurantListCreateAPIView(APIView):
    def get(self, request):
        # Gateway provides these headers after validating the JWT
        user_id = request.headers.get("user_id")
        role = request.headers.get("role", "").upper()

        # If no user_id, treat as public browsing
        if not user_id:
            queryset = Restaurant.objects.filter(is_active=True, is_open=True)
        elif role == "RESTAURANT_OWNER":
            queryset = Restaurant.objects.filter(owner_id=user_id)
        else:
            queryset = Restaurant.objects.filter(is_active=True)

        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = request.headers.get("user_id")
        role = request.headers.get("role", "").upper()

        if role != "RESTAURANT_OWNER":
            return Response({"detail": "Only owners can create restaurants"}, status=status.HTTP_403_FORBIDDEN)

        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner_id=user_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class AddRestaurantCategory(APIView):
    
    def post(self,request,pk):
        user_id = request.user.token.get("user_id")
        role = request.user.token.get("role","").upper()
        print(user_id)
        print(role)
        print("entering.......")
        if role != "RESTAURANT_OWNER":
            return Response({"detail": "Only owners can add categories"}, status=status.HTTP_403_FORBIDDEN)
        
        restaurant = get_object_or_404(Restaurant,id = pk)
        print(restaurant.owner_id)
        if str(restaurant.owner_id) != str(user_id):
            return Response({"error": "You do not own this restaurant"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant=restaurant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AddMenuItem(APIView):

    def post(self,request,pk):
        user_id = request.user.token.get("user_id")
        role = request.user.token.get("role","").upper()

        if role != "RESTAURANT_OWNER":
            return Response({"detail": "Only owners can add categories"}, status=status.HTTP_403_FORBIDDEN)
        
        category = get_object_or_404(Category,id=pk)

        if category.restaurant.owner_id != user_id:
            return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)