from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from .forms import CostumeUserCrateForm, CostumeUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CostumeUserCrateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserEditView(UpdateView):
    form_class = CostumeUserChangeForm
    template_name = 'profilePage/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class UserPageView(ListView):
    model = CustomUser
    template_name = 'profilePage/user_page.html'