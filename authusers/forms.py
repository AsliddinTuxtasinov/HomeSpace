from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Agents



class CostumeUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email',)


class CostumeUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email')


class AgentsEditForm(ModelForm):
    class Meta:
        model=Agents
        fields=('agent_info','telegram','facebook','twitter','linkedn')