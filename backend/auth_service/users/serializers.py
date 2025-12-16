from .models import User
from rest_framework import serializers


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