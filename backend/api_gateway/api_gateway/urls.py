from django.urls import path
from gateway.views import AuthProxy,RestaurantProxy,RestaurantCategoryProxy

urlpatterns = [
    path('auth/<path:path>/', AuthProxy.as_view()),
    path("restaurants/", RestaurantProxy.as_view()),
    path('restaurants/<path:path>/', RestaurantProxy.as_view()),
    path('categories/<path:path>/',RestaurantCategoryProxy.as_view())
]
