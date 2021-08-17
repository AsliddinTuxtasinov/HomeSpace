from django.contrib import admin
from .models import Posts,Regions,Districts,PostComment


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('title','price','year_build','owner','diller')


@admin.register(Regions)
class RegionAdmin(admin.ModelAdmin):
    pass
    # list_display = ['__all__']

@admin.register(Districts)
class DistrictAdmin(admin.ModelAdmin):
    pass
    # list_display = ['__all__']


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    pass