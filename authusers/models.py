from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    telefon_number = models.CharField(max_length=75,null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(
        'email address', unique=True,
        error_messages={
            'unique': "A user with that email already exists.",
        },)

    is_agent = models.BooleanField('agent',default=False,help_text=('is agent?'),)
    agent_info = models.TextField(max_length=300,null=True,blank=True)
    telegram = models.URLField(null=True,blank=True)


class Agents(models.Model):
    agent=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='agent')
    # profile_img=models.ImageField(upload_to='agents/profile_img')
    agent_info=models.TextField(max_length=300,null=True,blank=True)
    telegram = models.URLField(null=True,blank=True)

    def __str__(self):
        return f"Agent: {self.agent.first_name} {self.agent.last_name}"

    class Meta:
        verbose_name_plural = 'Agents'
        verbose_name = 'Agent'