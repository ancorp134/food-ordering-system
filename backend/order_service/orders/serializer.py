from .models import Order, OrderItem
from rest_framework import serializers
from django.db import transaction
import order_service.common.kafkaproducer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("menu_item_id", "quantity", "price")

        def validate_quantity(self, value):
            if value <= 0:
                raise serializers.ValidationError(
                    "Quantity must be greater than zero."
                )
            return value

        def validate_price(self, value):
            if value <= 0:
                raise serializers.ValidationError("Price must be greater than zero.")
            return value


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "restaurant_id",
            "total_amount",
            "status",
            "items",
            "created_at",
        )
        read_only_fields = (
            "id",
            "total_amount",
            "status",
            "created_at",
        )

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Order must contain at least one item.")
        return value

    @transaction.atomic
    def create(self, validated_data):

        request = self.context.get("request")
        customer_id = request.user.token.get("user_id")

        items_data = validated_data.pop("items")

        total_amount = sum(item["quantity"] * item["price"] for item in items_data)

        order = Order.objects.create(
            customer_id=customer_id,
            restaurant_id=validated_data["restaurant_id"],
            total_amount=total_amount,
            status="CREATED",
        )

        for item in items_data:
            OrderItem.objects.create(
                order=order,
                menu_item_id=item["menu_item_id"],
                quantity=item["quantity"],
                price=item["price"],
            )

        return order
