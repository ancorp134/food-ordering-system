from django.urls import path
from gateway.views import AuthProxy,RestaurantProxy,RestaurantCategoryProxy,CartProxy,OrderCheckoutProxy

urlpatterns = [
    path('auth/<path:path>/', AuthProxy.as_view()),
    path("restaurants/", RestaurantProxy.as_view()),
    path('restaurants/<path:path>/', RestaurantProxy.as_view()),
    path('categories/<path:path>/',RestaurantCategoryProxy.as_view()),
    path("cart/", CartProxy.as_view()),
    path("cart/items/", CartProxy.as_view()),
    path("cart/items/<uuid:item_id>/", CartProxy.as_view()),
    path("order/checkout/",OrderCheckoutProxy.as_view()),
    path("orders/me/",OrderCheckoutProxy.as_view()),

]
