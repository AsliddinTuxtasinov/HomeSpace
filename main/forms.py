from django import forms
from django_filters import FilterSet,NumberFilter
from .models import ContactWithAgent,SubscribeEmail,Posts,PostComment



class FilterHomeForm(FilterSet):
    price__lt = NumberFilter(field_name='price',lookup_expr='lt',label='Narxi kichikroq')
    price__gt=NumberFilter(field_name='price',lookup_expr='gt',label='Narxi kattaroq')

    year_build__lt = NumberFilter(field_name='year_build', lookup_expr='lt', label='shu yildan pastida qurilgan')
    year_build__gt = NumberFilter(field_name='year_build', lookup_expr='gt', label='shu yildan tepsida qurilgan')

    class Meta:
        model=Posts
        fields=('region','district',)


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


class PostCommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': '3','placeholder': 'Say Something...'}) )

    class Meta:
        model = PostComment
        fields = ['comment']