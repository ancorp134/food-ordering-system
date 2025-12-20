
from django.contrib import admin
from django.urls import path
from restaurant.views import RestaurantListCreateAPIView,AddRestaurantCategory,AddMenuItem

urlpatterns = [
    path("restaurants/", RestaurantListCreateAPIView.as_view()),
    path("restaurants/<uuid:pk>/categories/",AddRestaurantCategory.as_view()),
    path("categories/<uuid:pk>/menu-items/",AddMenuItem.as_view())
]
