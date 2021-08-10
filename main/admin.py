from django.contrib import admin

from .models import Posts,Regions,Districts,ContactWithAgent,SubscribeEmail

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('title','owner','diller')


@admin.register(Regions)
class RegionAdmin(admin.ModelAdmin):
    pass
    # list_display = ['__all__']

@admin.register(Districts)
class DistrictAdmin(admin.ModelAdmin):
    pass
    # list_display = ['__all__']

@admin.register(ContactWithAgent)
class ContactWithAgentAdmin(admin.ModelAdmin):
    list_display = ('post','agent','name','number')
    ordering = ['-created_at']

@admin.register(SubscribeEmail)
class SubscribeEmailAdmin(admin.ModelAdmin):
    # list_display = ('post','agent','name','number')
    ordering = ['-created_at']