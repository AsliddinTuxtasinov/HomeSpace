from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    telefon_number = models.CharField(max_length=75, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)