from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    email = models.EmailField(
        'email address', unique=True,
        error_messages={
            'unique': "A user with that email already exists.",},)
    is_agent = models.BooleanField('agent',default=False,help_text=('is agent?'),)
    create_date = models.DateTimeField(auto_now_add=True)


class Agents(models.Model):
    agent=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='agent')
    profile_img=models.ImageField(upload_to='agents/profile/img',null=True,blank=True)
    agent_info=models.TextField(max_length=300,default="No bio ...",blank=True)
    telefon_number = models.CharField(max_length=75, default="+998", blank=True)
    telegram = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    linkedn = models.URLField(null=True,blank=True)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.agent.first_name} {self.agent.last_name}"

    class Meta:
        verbose_name_plural = 'Agents'
        verbose_name = 'Agent'


class Founders(models.Model):
    founder=models.ForeignKey(Agents,on_delete=models.CASCADE,related_name='founder')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.founder.first_name} {self.founder.last_name}"

    class Meta:
        verbose_name_plural = 'Founders'
        verbose_name = 'Founder'