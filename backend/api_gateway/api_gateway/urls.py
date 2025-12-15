from django.urls import path
from gateway.views import AuthProxy

urlpatterns = [
    path('auth/<path:path>/', AuthProxy.as_view()),
]
