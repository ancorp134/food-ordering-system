from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True)

    class Meta :
        model = User
        fields = ('email','password','role')

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','role')




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["role"] = user.role
        return token
