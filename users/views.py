from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView

from .forms import CostumeUserCrateForm, CostumeUserChangeForm, PostCrateForm
from main.models import Posts


class PostCrateView(CreateView):
    model = Posts
    form_class = PostCrateForm
    template_name = 'blog/crate_post.html'
    # fields = '__all__'
    success_url = reverse_lazy('user_page')

    # def form_valid(self, form):
    #     form.owner = self.request.user
    #     return super().form_valid(form)



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
    model = Posts
    context_object_name = 'posts'
    template_name = 'profilePage/user_page.html'