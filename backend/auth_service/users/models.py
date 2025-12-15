from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('RESTAURANT_OWNER', 'Restaurant Owner'),
        ('CUSTOMER', 'Customer'),
        ('DELIVERY_AGENT', 'Delivery Agent'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects= UserManager()

    def __str__(self):
        return self.email
