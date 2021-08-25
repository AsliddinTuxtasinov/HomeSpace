from django import forms
from .models import Posts,Districts,PostComment



class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'
        exclude=('slug','owner','is_publish','is_send_mail')
        labels={ 'picture':'picture', 'picture2': 'picture-2', 'picture3': 'picture-3' }


    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['district'].queryset=Districts.objects.none()

        if 'region' in self.data:
            try:
                region_id=int(self.data.get('region'))
                self.fields['district'].queryset=Districts.objects.filter(region_id=region_id) #.order_by('district')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['district'].queryset=self.instance.region.district_set #.order_by('district')


class PostChageForm(forms.ModelForm):
    picture  = forms.ImageField(label='picture',  required=True, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    picture2 = forms.ImageField(label='picture-2',required=True ,widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    picture3 = forms.ImageField(label='picture-3',required=True, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model=Posts
        exclude = ('owner', 'slug', 'is_publish','is_send_mail')


class AgentPostChageForm(forms.ModelForm):
    class Meta:
        model=Posts
        exclude=('owner','slug','is_send_mail')
        labels = {'picture': 'picture', 'picture2': 'picture-2', 'picture3': 'picture-3'}


class PostCommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': '2','placeholder': 'Say Something...'}) )

    class Meta:
        model = PostComment
        fields = ['comment']