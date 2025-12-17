
from django.contrib import admin
from django.urls import path
from restaurant.views import RestaurantListCreateAPIView

urlpatterns = [
    path("restaurants/", RestaurantListCreateAPIView.as_view()),
]
