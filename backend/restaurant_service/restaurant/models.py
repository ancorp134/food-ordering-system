from django.db import models
import uuid
# Create your models here.

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner_id = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address_line_1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    cuisines = models.JSONField(default=list)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
