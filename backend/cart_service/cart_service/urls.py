from django.urls import path
from cart.views import CartAPIView, CartItemAPIView, CartItemDetailAPIView

urlpatterns = [
    path("cart/", CartAPIView.as_view()),
    path("cart/items/", CartItemAPIView.as_view()),
    path("cart/items/<uuid:item_id>/", CartItemDetailAPIView.as_view()),
]
