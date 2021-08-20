from django import forms
from django_filters import FilterSet,NumberFilter,ChoiceFilter

from .models import ContactWithAgent,SubscribeEmail
from announcement.models import Posts,PostComment



class FilterHomeForm(FilterSet):
    price__lt = NumberFilter(field_name='price',lookup_expr='lt',
            label='Narxi kichikroq',widget=forms.NumberInput(
            attrs={'placeholder': 'Narxi kichikroq (exmple: 140$)'} ))
    price__gt=NumberFilter(field_name='price',lookup_expr='gt',
            label='Narxi kattaroq',widget=forms.NumberInput(
            attrs={'placeholder': 'Narxi kattaroq (exmple: 140$)'} ))
    
    area__lt = NumberFilter(field_name='area',lookup_expr='lt',
            label='maydoni kichikroq',widget=forms.NumberInput(
            attrs={'placeholder': 'maydoni kichikroq (exmple: <40 m.kv)'} ))
    area__gt=NumberFilter(field_name='area',lookup_expr='gt',
            label='maydoni kattaroq',widget=forms.NumberInput(
            attrs={'placeholder': 'maydoni kattaroq (exmple: <40 m.kv)'} ))


    year_build__lt = NumberFilter(field_name='year_build', lookup_expr='lt',
            label='shu yildan pastida qurilgan',widget=forms.NumberInput(
            attrs={'placeholder': 'qurilgan yili kichik (exmple: <2006)'}))
    year_build__gt = NumberFilter(field_name='year_build', lookup_expr='gt',
            label='shu yildan tepsida qurilgan',widget=forms.NumberInput(
            attrs={'placeholder': 'qurilgan yili kattaroq (exmple: >2006)'}))

    class Meta:
        model=Posts
        fields=('home_type','type','region','district','type')


class ContactWithAgentForm(forms.ModelForm):
    class Meta:
        model = ContactWithAgent
        fields = ('name','email','number')
        widgets={
            'name'  : forms.TextInput(attrs={'class':'form-control'},),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control','placeholder':'+998901234567'})
        }


class SubscribeForm(forms.ModelForm):
    email=forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'asliddintukhtasinov5@gmail.com'}))

    class Meta:
        model=SubscribeEmail
        fields=['email',]