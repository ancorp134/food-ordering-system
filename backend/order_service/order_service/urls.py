from orders.views import OrderCheckOut
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('order/checkout/',OrderCheckOut.as_view()),
]
