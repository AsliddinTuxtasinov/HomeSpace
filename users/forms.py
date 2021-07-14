from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CostumeUserCrateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email',) # UserCreationForm.Meta.fields + ('telefon_number',)



class CostumeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','telefon_number') # UserChangeForm.Meta.fields

