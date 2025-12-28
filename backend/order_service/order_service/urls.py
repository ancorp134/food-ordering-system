from orders.views import OrderCheckOut, CustomerOrderView,CustomerOrder,HealthCheckView
from django.contrib import admin
from django.urls import path
# from health.views import HealthCheckView


urlpatterns = [
    path('order/checkout/',OrderCheckOut.as_view()),
    path('orders/me/',CustomerOrderView.as_view()),
    path('orders/me/<uuid:pk>/',CustomerOrder.as_view()),
    path('health/',HealthCheckView.as_view())
]
