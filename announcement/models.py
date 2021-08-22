from os import remove
from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

from django.contrib.auth import get_user_model
User = get_user_model()

from authusers.models import Agents



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
    resturant='resturant'; market='market'; float='float'; yard='yard'
    type = [ (resturant, 'resturant'),(market,'market'),(float, 'float'),(yard, 'yard') ]

    sale = 'buy'; rent = 'rent'
    type_status = [ (sale, 'Buy'),(rent, 'Rent') ]
    ### 
    title      = models.CharField(max_length=255,unique=True)
    home_type  = models.CharField(max_length=20, choices=type, default=type[2][0])
    type = models.CharField(max_length=20, choices=type_status, default=type_status[0][0])
    price      = models.FloatField('price ($)', default=0, blank=True,validators=[MinValueValidator(0)])
    year_build = models.PositiveIntegerField(default=0,blank=True,validators=[MinValueValidator(0)])
    more_info  = models.TextField('more info',default="more info ...")
    area       = models.FloatField('area (m.kv)',default=1)
    picture = models.ImageField(
        upload_to=f"announcement/%Y/%m/%d/announcement")
    picture2   = models.ImageField(
        upload_to=f"announcement/%Y/%m/%d/announcement")
    picture3   = models.ImageField(
        upload_to=f"announcement/%Y/%m/%d/announcement")
    beds = models.PositiveIntegerField(
        'badroom',validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    baths = models.PositiveIntegerField(
        'batheroom',validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    garages = models.PositiveIntegerField(
        'garages',validators=[MinValueValidator(0), MaxValueValidator(5)],default=1)
    tel_num = models.CharField("telefon number:",max_length=40,default="+998")
    region     = models.ForeignKey(Regions,on_delete=models.CASCADE)
    district   = models.ForeignKey(Districts,on_delete=models.CASCADE)
    adress     = models.CharField(max_length=255,null=True)
    diller     = models.ForeignKey(Agents,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, db_index=True,blank=True)

    owner      = models.ForeignKey(User, on_delete=models.CASCADE)
    is_publish = models.BooleanField(default=False)
    is_send_mail = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def delete(self, *args, **kwargs):
        self.picture.delete()
        self.picture2.delete()
        self.picture3.delete()
        super().delete(*args, **kwargs)



    def get_absolute_url(self):
        kwargs = { 'slug': self.slug }
        return reverse('post-detail', kwargs=kwargs)

    def get_absolute_url_edit(self):
        kwargs = { 'slug': self.slug }
        return reverse('post-edit', kwargs=kwargs)

    def get_absolute_url_delete(self):
        kwargs = { 'slug': self.slug }
        return reverse('post-delete', kwargs=kwargs)

    def get_absolute_url_comment(self):
        kwargs = { 'slug': self.slug }
        return reverse('comment', kwargs=kwargs)

    def get_contact_with_agent_url(self):
        kwargs = { 'slug': self.slug }
        return reverse('main:contact', kwargs=kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'


class PostComment(models.Model):
    comment = models.TextField("your comment:")
    parent = models.ForeignKey('self', null=True,blank=True, related_name='replies',on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} | {self.author} | comment"