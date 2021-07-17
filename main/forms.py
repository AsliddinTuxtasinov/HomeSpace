from django import forms
from .models import Posts


class PostChageForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=('title',)