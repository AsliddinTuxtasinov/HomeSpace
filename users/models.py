from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.validators import UnicodeUsernameValidator

class CustomUser(AbstractUser):
    telefon_number = models.CharField(max_length=75, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    # email_validator = UnicodeUsernameValidator()
    email = models.EmailField(
        'email address', unique=True,
        # validators=[email_validator],
        error_messages={
            'unique': "A user with that email already exists.",
        },)