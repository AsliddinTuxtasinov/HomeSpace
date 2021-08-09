from django.forms import ModelForm,TextInput,EmailInput
from django_filters import FilterSet
from .models import ContactWithAgent,Posts

class FilterHomeForm(FilterSet):
    class Meta:
        model=Posts
        fields=['region','district']


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
