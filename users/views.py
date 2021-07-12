from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CostumeUserCrateForm


class SignUpView(CreateView):
    form_class = CostumeUserCrateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
