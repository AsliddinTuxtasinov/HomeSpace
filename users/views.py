# from django.shortcuts import render, redirect  # second way for create post
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, View

from .forms import CostumeUserCreateForm, CostumeUserChangeForm, PostCreateForm
from main.models import Posts


# first way for create post
class PostCreateView(CreateView):
    form_class = PostCreateForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy("user_page")


    def form_valid(self,form):
        self.object = form.save(commit=False)
        form.instance.owner = self.request.user
        return super().form_valid(form)

# second way for create post
# class PostCreateView(View):
#     form_class = PostCreateForm
#     template_name = 'blog/create_post.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(data=request.POST)
#         if form.is_valid():
#             qs = form.save(commit=False)
#             qs.owner = self.request.user
#             qs.save()
#             return redirect('user_page')
#         return render(request, self.template_name, {'form': form})


class SignUpView(CreateView):
    form_class = CostumeUserCreateForm
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

    def get_queryset(self):
        queryset = self.model._default_manager.filter(owner=self.request.user)
        return queryset