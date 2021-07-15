# from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from main.models import Posts

class CostumeUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email',)


class CostumeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','telefon_number')

class PostCreateForm(ModelForm):
    class Meta:
        model = Posts
        fields = ('title',)