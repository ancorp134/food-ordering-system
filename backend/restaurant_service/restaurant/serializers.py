from .models import Restaurant,MenuItem,Category
from rest_framework import serializers


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        read_only_fields = ('category',)

class CategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        fields = ('id','name','items')
class RestaurantSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many = True,read_only=True)
    class Meta:
        model = Restaurant
        fields = (
            "id",
            "name",
            "description",
            "owner_id",
            "is_active",
            "is_open",
            "phone_number",
            "address_line_1",
            "city",
            "state",
            "pincode",
            "cuisines",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
            "categories"
        )
        read_only_fields = ("id", "owner_id", "created_at", "updated_at")