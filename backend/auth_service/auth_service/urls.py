from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import RegisterView,MeView,CustomTokenObtainPairView

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', CustomTokenObtainPairView.as_view()),
    path('auth/me/', MeView.as_view()),
]
