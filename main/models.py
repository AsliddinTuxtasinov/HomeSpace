from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()
from users.models import Agents

# from django.conf import settings
# User = settings.AUTH_USER_MODEL

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Regions(models.Model):
    region = models.CharField(max_length=150)

    def __str__(self):
        return self.region

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'


class Districts(models.Model):
    region=models.ForeignKey( Regions,on_delete=models.CASCADE )
    district = models.CharField(max_length=150)

    def __str__(self):
        return self.district

    class Meta:
        verbose_name_plural = 'Districts'
        verbose_name = 'District'


class Posts(models.Model):
    # resturant = 'resturant'
    # market    = 'market'
    # float     = 'float'
    # hovli     = 'hovli'  # to'girlab ketiladi inglizchaga
    # type = [
    #     (resturant, 'resturant'),
    #     (market,'market'),
    #     (float, 'float'),
    #     (hovli, 'hovli')
    # ]
    # sale = 'sale'
    # rent = 'rent'
    # type_status = [
    #     (sale,'sale'),
    #     (rent,'rent')
    # ]
    title       = models.CharField(max_length=255,unique=True)
    # full_adress = models.CharField('full adress',max_length=255)
    # home_type   = models.CharField(max_length=20, choices=type)
    # price       = models.FloatField('price', default=0, blank=True)
    # year_build  = models.IntegerField()
    # more_info   = models.TextField('more info')
    # area        = models.FloatField('area')
    # picture     = models.ImageField(upload_to=f"anouncment/{self.title}/posts")
    # picture2    = models.ImageField(upload_to=f"anouncment/{self.title}/posts", blank=True,null=True)
    # picture3    = models.ImageField(upload_to=f"anouncment/{self.title}/posts",blank=True,null=True)
    # beds        = models.IntegerField('badroom',validators=[MinValueValidator(1), MaxValueValidator(5)])
    # baths       = models.IntegerField('batheroom',validators=[MinValueValidator(1), MaxValueValidator(5)])
    # baths = models.IntegerField('garages', validators=[MinValueValidator(0), MaxValueValidator(5)])
    # property_status = models.CharField(max_length=20,choices=type_status)
    # tel_num = models.CharField("telefon number:",max_length=150)
    region        = models.ForeignKey(Regions,on_delete=models.CASCADE,null=True)#default='somewhere in uzbesistan')
    district      = models.ForeignKey(Districts,on_delete=models.CASCADE,null=True)#default='somewhere in uzbesistan')
    adress        = models.CharField(max_length=255,null=True)
    diller        = models.ForeignKey(Agents,on_delete=models.SET_NULL,null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, db_index=True,blank=True)

    owner      = models.ForeignKey(User, on_delete=models.CASCADE)
    is_publish = models.BooleanField(default=False)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        kwargs = { 'slug': self.slug }
        return reverse('main:property', kwargs=kwargs)

    def get_absolute_url_edit(self):
        kwargs = { 'slug': self.slug }
        return reverse('property-edit', kwargs=kwargs)

    def get_absolute_url_delete(self):
        kwargs = { 'slug': self.slug }
        return reverse('property-delete', kwargs=kwargs)

    def get_contact_with_agent_url(self):
        kwargs = { 'slug': self.slug }
        return reverse('main:contact', kwargs=kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'

class ContactWithAgent(models.Model):
    post  = models.ForeignKey(Posts,on_delete=models.CASCADE,blank=False)
    agent = models.ForeignKey(Agents,on_delete=models.CASCADE,blank=False)
    name  = models.CharField(max_length=150,blank=False)
    email = models.EmailField(blank=False)
    number= models.CharField(max_length=50,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post}|{self.name}|{self.number}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contac tWith Agent'

# class PostComment(models.Model):
#     Full_name=models.CharField("your full name:", max_length=255)
#     comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.TextField("your comment:")



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