from django.db import models
from django.urls import reverse

from announcement.models import Posts
from authusers.models import Agents


class Contact(models.Model):
    full_name = models.CharField(max_length=180, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=255, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']


class ContactWithAgent(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=False)
    number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url_delete(self):
        kwargs = {'pk': self.id}
        return reverse('contact_delete', kwargs=kwargs)

    def __str__(self):
        return f"{self.post}|{self.name}|{self.number}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Contacts With Agent'
        verbose_name = 'Contact With Agent'


class SubscribeEmail(models.Model):
    email = models.EmailField("Your email", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} was subscrbied at {self.created_at}"

# it is not necessary now
# class AboutOurs(models.Model):
#     our_company = models.TextField()
#     pic_company = models.ImageField(upload_to='aboutOurs/about_picture')
#     our_office = models.TextField()
#     pic_office = models.ImageField(upload_to='aboutOurs/about_picture')
#     adress = models.CharField()
#     about_homespace = models.TextField(max_length=300)
#
#     telefon = models.CharField(max_length=150)
#     gmail = models.EmailField()
#     facebook = models.URLField(default='#', null=False)
#     telegram = models.URLField(default='#', null=False)
#     instagram = models.URLField(default='#', null=False)
