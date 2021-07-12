from django.db import models

# from django.contrib.auth.models import User
# from django.core.validators import MinValueValidator, MaxValueValidator
# # from django.utils.text import slugify # kiyinchalik client e'lon berganda ishlatilinishi mumkin
#
#
# class Posts(models.Model):
#     resturant = 'resturant'
#     market    = 'market'
#     float     = 'float'
#     hovli     = 'hovli'  # to'girlab ketiladi inglizchaga
#     type = [
#         (resturant, 'resturant'),
#         (market,'market'),
#         (float, 'float'),
#         (hovli, 'hovli')
#     ]
#     sale = 'sale'
#     rent = 'rent'
#     type_status = [
#         (sale,'sale'),
#         (rent,'rent')
#     ]
#
#     title       = models.CharField(max_length=255,unique=True)
#     full_adress = models.CharField('full adress',max_length=255)
#     home_type   = models.CharField(max_length=20, choices=type)
#     price       = models.FloatField('price', default=0, blank=True)
#     year_build  = models.IntegerField()
#     more_info   = models.TextField('more info')
#     area        = models.FloatField('area')
#     picture     = models.ImageField(upload_to=f"anouncment/{self.title}/posts")
#     picture2    = models.ImageField(upload_to=f"anouncment/{self.title}/posts", blank=True,null=True)
#     picture3    = models.ImageField(upload_to=f"anouncment/{self.title}/posts",blank=True,null=True)
#     beds        = models.IntegerField('badroom',validators=[MinValueValidator(1), MaxValueValidator(5)])
#     baths       = models.IntegerField('batheroom',validators=[MinValueValidator(1), MaxValueValidator(5)])
#     baths = models.IntegerField('garages', validators=[MinValueValidator(0), MaxValueValidator(5)])
#     property_status = models.CharField(max_length=20,choices=type_status)
#     tel_num = models.CharField("telefon number:",max_length=150)
#     created_at      = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(max_length=255, db_index=True, blank=True, null=True)
#
#     owner       = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_done     = models.BooleanField('is it done for print?', bool=False)
#
#
#     # def save(self, *args, **kwargs):
#     #     self.slug = slugify(self.title)
#     #     super().save(*args,**kwargs)
#
#     def __str__(self):
#         return f"{self.title}|{self.home_type}|{self.price}"
#
#
# # class PostComment(models.Model):
# #     Full_name=models.CharField("your full name:", max_length=255)
# #     comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
# #     comment = models.TextField("your comment:")
#
# class OurAgents(models.Model):
#     agent = models.ForeignKey(User,on_delete=models.CASCADE)
#     ixtisoslik = models.CharField(max_length=200) # inglizchaga ozgartirish kerak
#     agent_info = models.TextField(max_length=300)
#     facebook = models.URLField(default='#', null=False)
#     telegram = models.URLField(default='#', null=False)
#     instagram = models.URLField(default='#', null=False)
#
#
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