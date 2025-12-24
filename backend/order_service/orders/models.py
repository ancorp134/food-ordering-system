from django.db import models
import uuid
# Create your models here.

class Order(models.Model):

    STATUS_CHOICES = (
        ("CREATED", "Created"),
        ("CONFIRMED", "Confirmed"),
        ("PREPARING", "Preparing"),
        ("OUT_FOR_DELIVERY", "Out for Delivery"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    )

    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    customer_id = models.UUIDField()
    restaurant_id = models.UUIDField()

    status =  models.CharField(max_length=100,choices=STATUS_CHOICES,default="CREATED")

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id}"
