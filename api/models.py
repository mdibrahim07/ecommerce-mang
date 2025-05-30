from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)  # For admin-specific access

    def __str__(self):
        return self.username

# Customer Profile
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
