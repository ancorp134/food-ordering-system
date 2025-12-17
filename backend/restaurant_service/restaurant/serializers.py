from .models import Restaurant
from rest_framework import serializers

class RestaurantSerializer(serializers.ModelSerializer):

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
        )
        read_only_fields = ("id", "owner_id", "created_at", "updated_at")