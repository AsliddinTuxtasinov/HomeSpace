# from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser,Agents
from main.models import Posts,Districts

# ===================================================================================== #
class CostumeUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email',)

class CostumeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','telefon_number')

class AgentsEditForm(ModelForm):
    class Meta:
        model=Agents
        fields=('agent_info','telegram')

# ===================================================================================== #
# Post forms
class PostCreateForm(ModelForm):
    class Meta:
        model = Posts
        fields = ('title','region','district','adress','diller')

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['district'].queryset=Districts.objects.none()

        if 'region' in self.data:
            try:
                region_id=int(self.data.get('region'))
                self.fields['district'].queryset=Districts.objects.filter(region_id=region_id)#.order_by('district')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['district'].queryset=self.instance.region.district_set#.order_by('district')

class PostChageForm(ModelForm):
    class Meta:
        model=Posts
        fields=('title','region','district','adress','diller')