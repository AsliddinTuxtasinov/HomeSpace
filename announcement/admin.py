from django.contrib import admin
from .models import Posts,Regions,Districts,PostComment



@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('title','price','year_build','owner','diller')


@admin.register(Regions)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['region']


@admin.register(Districts)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['region','district']


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    pass