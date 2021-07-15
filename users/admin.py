from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CostumeUserCreateForm, CostumeUserChangeForm
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CostumUserAdmin(UserAdmin):
    add_form = CostumeUserCreateForm
    form = CostumeUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'telefon_number' ,'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('telefon_number',),
        }),
    )

    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {
    #         'fields': ('telefon_number',),
    #     }),
    # )