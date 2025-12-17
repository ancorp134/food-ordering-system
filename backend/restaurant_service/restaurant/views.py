from django.urls import path
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.user.token
        role = token.get("role")
        user_id = token.get("user_id")

        if not role:
            return Response(
                {"detail": "Role missing in token"},
                status=status.HTTP_403_FORBIDDEN
            )

        role = role.upper()

        if role == "CUSTOMER":
            queryset = Restaurant.objects.filter(is_active=True)

        elif role == "RESTAURANT_OWNER":
            queryset = Restaurant.objects.filter(owner_id=user_id)

        else:
            return Response(
                {"detail": "Invalid role"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        token = request.user.token
        role = token.get("role")
        user_id = token.get("user_id")

        if role != "RESTAURANT_OWNER":
            return Response(
                {"detail": "Access denied"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner_id=user_id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
