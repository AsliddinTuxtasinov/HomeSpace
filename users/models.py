from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    telefon_number = models.CharField(
        max_length=75,
        null=True,
        blank=True
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )

    email = models.EmailField(
        'email address', unique=True,
        error_messages={
            'unique': "A user with that email already exists.",
        },)

    is_agent = models.BooleanField(
        'agent',default=False,help_text=('is agent?'),
    )
    agent_info = models.TextField(
        max_length=300,null=True,blank=True
    )
    telegram = models.URLField(
        null=True,blank=True
    )


# ortiqcha jadval ochirib tashlanadi kiyinchalik
from django.contrib.auth import get_user_model # ochiriladi bu ham
class Agents(models.Model):
    agent=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='agent'
    )
    agent_info=models.TextField(
        max_length=300
    )
    telegram = models.URLField()

    def __str__(self):
        return f"Agent: {self.agent}"

    class Meta:
        verbose_name_plural = 'Agents'
        verbose_name = 'Agent'