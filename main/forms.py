from django.forms import ModelForm,TextInput,EmailInput
from django_filters import FilterSet,NumberFilter
from .models import ContactWithAgent,SubscribeEmail,Posts ,Districts

class FilterHomeForm(FilterSet):
    price__lt = NumberFilter(field_name='price', lookup_expr='lt', label='Narxi kichikroq')
    price__gt=NumberFilter(field_name='price',lookup_expr='gt',label='Narxi kattaroq')

    year_build__lt = NumberFilter(field_name='year_build', lookup_expr='lt', label='shu yildan pastida qurilgan')
    year_build__gt = NumberFilter(field_name='year_build', lookup_expr='gt', label='shu yildan tepsida qurilgan')

    class Meta:
        model=Posts
        fields=('region','district',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['district'].queryset = Districts.objects.none()
    #
    #     if 'region' in self.data:
    #         try:
    #             region_id = int(self.data.get('region'))
    #             self.fields['district'].queryset = Districts.objects.filter(region_id=region_id)
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['district'].queryset = self.instance.region.district_set


class ContactWithAgentForm(ModelForm):
    # name=TextInput(
    #     attrs={'class': 'form-control'},
    #     error_messages={'required': 'please fill in the blanks'}
    # ),
    # email=EmailInput(
    #     attrs={'class': 'form-control'},
    #     error_messages={'required': 'please fill in the blanks'}
    # ),
    # number=TextInput(
    #     attrs={'class': 'form-control','placeholder': '+998901234567'}
    # )

    class Meta:
        model = ContactWithAgent
        fields = ('name','email','number')
        widgets={
            'name':TextInput(
                attrs={'class':'form-control'},
                # error_messages={'required': 'please fill in the blanks'}
            ),
            'email':EmailInput(
                attrs={'class': 'form-control'}
            ),
            'number':TextInput(
                attrs={'class': 'form-control','placeholder':'+998901234567'}
            )
        }


        # def __init__(self):
        #     super(ContactWithAgentForm,self).__init__(*args,**kvargs)
        #     self.fields['name'].error_messages['required']='please fill in the blanks'


class SubscribeForm(ModelForm):
    class Meta:
        model=SubscribeEmail
        fields=['email',]