from django.contrib import admin

from .models import Posts,Regions,Districts

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('title','owner')

@admin.register(Regions)
class RegionAdmin(admin.ModelAdmin):
    pass
    # list_display = ['__all__']

@admin.register(Districts)
class DistrictAdmin(admin.ModelAdmin):
    pass
    # list_display = ['__all__']