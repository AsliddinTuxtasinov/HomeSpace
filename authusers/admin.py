from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


from .forms import CostumeUserCreateForm, CostumeUserChangeForm
from .models import CustomUser,Agents,Founders

# Register your models here.
@admin.register(CustomUser)
class CostumUserAdmin(UserAdmin):
    add_form = CostumeUserCreateForm
    form = CostumeUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name','is_staff','is_agent')

    fieldsets = UserAdmin.fieldsets + (
        # (None, {
        #     'fields': ('agent_info','telegram'),
        # }),
        
        (_('Permissions'), {
            'fields': ('is_agent',),
        }),
    )

    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {
    #         'fields': ('telefon_number',),
    #     }),
    # )

@admin.register(Agents)
class AgentAdmin(admin.ModelAdmin):
    list_display=('agent','telefon_number','telegram')


@admin.register(Founders)
class FounderAdmin(admin.ModelAdmin):
    list_display=('founder',)