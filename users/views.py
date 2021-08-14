from django.shortcuts import render, redirect  # second way for create post
from django.urls import reverse_lazy,reverse
from django.core.mail import send_mail,EmailMultiAlternatives # for send message to mail
from django.contrib import messages
from django.views.generic import UpdateView, ListView, CreateView, DeleteView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()

from .forms import CostumeUserCreateForm, CostumeUserChangeForm, PostCreateForm, PostChageForm,AgentsEditForm,AgentPostChageForm
from main.forms import PostCommentForm
from main.models import Posts,Districts,ContactWithAgent,SubscribeEmail,PostComment
from .models import Agents

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

    def get_form_class(self):
        client=self.request.user
        if client.is_agent:
            return AgentPostChageForm
        else:
            return self.form_class


    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.is_publish and self.request.user.is_agent and self.object.is_send_mail==False:
            link=f"http://127.0.0.1:8000/property/{self.object.slug}/" # this is not perfect way. In the future may be repair it
            title = self.object.title
            message=f"""
                Yangi ajoyib uy e'lonlar safiga qo'yildi :)\n
                siz bu e'lonni quydagi havola roqali ko'rishingiz mumkin\n
                 -> {link}"""
            emails=[''.join(i.email) for i in SubscribeEmail.objects.all()]
            print(emails)

            try:
                send_mail(title,message,'',emails,fail_silently=False,)
            except:
                messages.error(self.request, "serverga ulanishda xatobor iltimos boshqatan urinib ko'ring !")
                return redirect(self.request.path)
            form.instance.is_send_mail=True

        self.object = form.save()
        return super().form_valid(form)

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

# Post comment create
# class PostCommentView(CreateView):
#     # model = PostComment
#     queryset = Posts
#     form_class = PostCommentForm
#     # template_name = 'property-details.html'
#
#
#     def get_object(self, queryset=None):
#         queryset = self.queryset
#         slug = self.kwargs.get(self.slug_url_kwarg)
#         # queryset = queryset.filter(pk=pk)
#         obj = queryset.get(**{slug_field: slug})
#         # obj = queryset.get()
#         return obj
#
#     def post(self, request, *args, **kwargs):
#         form=self.form_class(data=request.POST)
#         if form.is_valid():
#             qs=form.save(commit=False)
#             qs.author=self.request.user
#             qs.post = self.get_object()
#             qs.save()
#             messages.success(request,"muofuqiyatli comment qoldirdingiz")
#             return redirect(self.request.path)
#         messages.error(request, "iltimos boshqattan urinib ko'ring")
#         return redirect(self.request.path)

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

# Contact With Client View
class ContactWithClientView(LoginRequiredMixin,ListView):
    model = ContactWithAgent
    context_object_name = 'contacts'
    template_name = 'profilePage/contact_with_client.html'
    paginate_by = 4


    def get_queryset(self):
        client = self.request.user
        if client.is_authenticated:
            diller=Agents.objects.get(agent=client)
            queryset = self.model._default_manager.filter(agent=diller)
            return queryset
        return None

# user edit data view
class UserEditView(View):
    form_class = CostumeUserChangeForm
    form_class_agent = AgentsEditForm
    template_name = 'profilePage/edit_profile.html'
    success_url = reverse_lazy('user_page')

    def get(self, request):
        context={}
        context['form']=self.form_class(instance=request.user)
        if request.user.is_agent:
            agent=Agents.objects.get(agent=request.user)
            context['form_agent'] = self.form_class_agent(instance=agent)
        return render(request,self.template_name,context)

    def post(self,request):
        context={}
        form=self.form_class(request.POST,instance=request.user)
        if request.user.is_agent:
            agent = Agents.objects.get(agent=request.user)
            form_agent=self.form_class_agent(request.POST,instance=agent)

            if form.is_valid() and form_agent.is_valid():
                form.save()
                form_agent.save()
                return redirect('user_page')
            context['form_agent'] = form_agent
        else:
            if form.is_valid():
                form.save()
                return redirect('user_page')

            context['form_agent'] = None
        context['form']=form
        return render(request, self.template_name, context)

# class UserEditView(UpdateView):
#     form_class = CostumeUserChangeForm
#     template_name = 'profilePage/edit_profile.html'
#     success_url = reverse_lazy('index')
#
#     def get_object(self):
#         return self.request.user



# user page view
class UserPageView(LoginRequiredMixin,ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'profilePage/user_page.html'
    paginate_by = 6
    paginate_orphans = 3

    def get_queryset(self):
        client = self.request.user
        if client.is_agent:
            diller=Agents.objects.get(agent=client)
            queryset = self.model._default_manager.filter(diller=diller)
        else:
            queryset = self.model._default_manager.filter(owner=client)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        client = self.request.user
        if client.is_agent:
            context['contact_with_cilent_count']=len(ContactWithAgent.objects.filter(agent__agent=client))
        return context