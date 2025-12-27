from orders.views import OrderCheckOut, CustomerOrderView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('order/checkout/',OrderCheckOut.as_view()),
    path('orders/me/',CustomerOrderView.as_view()),
]
