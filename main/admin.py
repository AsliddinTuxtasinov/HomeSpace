from django.contrib import admin

from .models import Posts
@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('title','owner')