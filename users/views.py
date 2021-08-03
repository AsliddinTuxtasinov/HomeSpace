from django.shortcuts import render, redirect  # second way for create post
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CostumeUserCreateForm, CostumeUserChangeForm, PostCreateForm, PostChageForm
from main.models import Posts,Districts

# =============================== post views =============================== #
# Post delete view
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Posts
    template_name='blog/posts_confirm_delete.html'
    success_url = reverse_lazy('user_page')
    context_object_name = 'post'

# Post chahge view
class PostChageView(LoginRequiredMixin,UpdateView):
    model = Posts
    form_class = PostChageForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('user_page')
    context_object_name = 'post'

# first way for create post
class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = PostCreateForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy("user_page")


    def form_valid(self,form):
        self.object = form.save(commit=False)
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create_post"]=True
        return context

# AJAX
def load_cities(request):
    region_id = request.GET.get('region_id')
    districts = Districts.objects.filter(region_id=region_id)
    return render(request, 'blog/city_dropdown_list_options.html', {'districts': districts})

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


# =============================== user views =============================== #
# Sign up view
class SignUpView(CreateView):
    form_class = CostumeUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# user edit data view
class UserEditView(UpdateView):
    form_class = CostumeUserChangeForm
    template_name = 'profilePage/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

# user page view
class UserPageView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'profilePage/user_page.html'
    paginate_by = 9
    paginate_orphans = 3

    def get_queryset(self):
        owner = self.request.user
        queryset = self.model._default_manager.filter(owner=owner)
        return queryset