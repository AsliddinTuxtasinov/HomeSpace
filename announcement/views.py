import os
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail  # for send message to mail
from django.contrib import messages
from django.views.generic import UpdateView,CreateView,DeleteView,DetailView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()


from .forms import PostCreateForm,PostChageForm,AgentPostChageForm,PostCommentForm
from main.forms import ContactWithAgentForm,SubscribeEmail
from .models import Posts,Districts,PostComment


# first way for create post
class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy("user_page")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.owner = self.request.user
        self.object = form.save()
        return super(PostCreateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create_post"] = True
        return context


# Post chahge view
class PostChageView(LoginRequiredMixin, UpdateView):
    model = Posts
    form_class = PostChageForm
    template_name = 'blog/create_post.html'
    context_object_name = 'post'


    def get_form_class(self):
        client = self.request.user
        if client.is_agent:
            return AgentPostChageForm
        else:
            return self.form_class


    # this method add for delete old pictures in media files
    def get_old_object(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        old_obj = Posts.objects.get(slug=slug)
        old_pic={
            'picture' :old_obj.picture.path,
            'picture2':old_obj.picture2.path,
            'picture3':old_obj.picture3.path,
        }
        return old_pic


    def form_valid(self, form):
        old_obj_pics=self.get_old_object() # => dict
        self.object = form.save(commit=False)

        # if agent permits publish
        if self.object.is_publish and self.request.user.is_agent and self.object.is_send_mail == False:
            link = f"http://127.0.0.1:8000/property/{self.object.slug}/"  # this is not perfect way. In the future may be repair it
            title = self.object.title
            message = f"""Yangi ajoyib uy e'lonlar safiga qo'yildi :)\nsiz bu e'lonni quydagi havola roqali ko'rishingiz mumkin\n-> {link}"""
            emails = [''.join(i.email) for i in SubscribeEmail.objects.all()]
            print(emails)

            try:
                send_mail(title, message, '', emails, fail_silently=False, )
            except:
                messages.error(self.request, "serverga ulanishda xatobor iltimos boshqatan urinib ko'ring !")
                return redirect(self.request.path)
            form.instance.is_send_mail = True

        # if pictures are update
        if self.request.FILES.get('picture'):
            os.remove(old_obj_pics['picture'])
        if self.request.FILES.get('picture2'):
            os.remove(old_obj_pics['picture2'])
        if self.request.FILES.get('picture3'):
            os.remove(old_obj_pics['picture3'])

        self.object = form.save()
        return super().form_valid(form)


    def get_success_url(self):
        url = self.object.get_absolute_url()
        return url


# Post delete view
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'blog/posts_confirm_delete.html'
    success_url = reverse_lazy('user_page')
    context_object_name = 'post'

class DetailPageView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'property-details.html'

    def get_context_data(self,*args, **kwargs):
        obj=self.get_object()
        client=self.request.user
        agent=False

        if client.is_authenticated:
            agent=client.is_agent
        owner = self.object.owner == client

        context = super().get_context_data()
        context['posts'] = self.model.objects.filter(region=obj.region,district=obj.district, created_at__gt=obj.created_at)[0:3]
        context['contact_with_agent_form'] = ContactWithAgentForm
        context['post_commentform'] = PostCommentForm
        context['comments'] = PostComment.objects.filter(post=self.object,parent=None)
        context['is_author_or_agent'] = True if agent or owner else False
        return context

# AJAX
def load_cities(request):
    region_id = request.GET.get('region_id')
    districts = Districts.objects.filter(region_id=region_id)
    return render(request, 'blog/city_dropdown_list_options.html', {'districts': districts})


# Post comment create
class PostCommentView(LoginRequiredMixin,View):
    form_class = PostCommentForm

    def post(self, request,slug, *args, **kwargs):
        post = get_object_or_404(Posts,slug=slug)
        form = self.form_class(data=request.POST)

        if form.is_valid():
            reply_obj = None
            try:
                reply_id=int(request.POST.get('parent_id'))
            except:
                reply_id=None

            if reply_id:
                reply_obj=get_object_or_404(PostComment,id=reply_id)

            qs = form.save(commit=False)
            qs.author = request.user
            qs.post = post
            if reply_obj: qs.parent=reply_obj
            qs.save()
            messages.success(request, "muofuqiyatli comment qoldirdingiz")
            return redirect(post.get_absolute_url())

        messages.error(request, "iltimos boshqattan urinib ko'ring")
        return redirect(reverse('post-detail', kwargs={'slug': slug}))


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
