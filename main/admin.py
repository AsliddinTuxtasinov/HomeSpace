from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ContactWithAgent,SubscribeEmail,Contact


admin.site.unregister(Group)

@admin.register(ContactWithAgent)
class ContactWithAgentAdmin(admin.ModelAdmin):
    list_display = ('post','name','number')
    ordering = ['-created_at']


@admin.register(SubscribeEmail)
class SubscribeEmailAdmin(admin.ModelAdmin):
    # list_display = ('post','agent','name','number')
    ordering = ['-created_at']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['full_name','subject']
    ordering = ['-created_at']