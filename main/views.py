from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PostChageForm
from .models import Posts


class HomePageView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['objs']       = [i for i in range(9)]
        context['our_blog']   = [i for i in range(3)]
        context['main_posts'] = Posts.objects.all()[0:3]
        context['main_page']  = True
        return context

class BlogPageView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['objs'] = [i for i in range(9)]
        context['our_blog'] = [i for i in range(6)]
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['testers'] = [i for i in range(9)]
        context['leaders'] = [200,300,400,400,200,300]
        return context

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['testers'] = [i for i in range(9)]
        # context['leaders'] = [200,300,400,400,200,300]
        return context



class PropertiesPageView(ListView):
    model=Posts
    context_object_name = 'posts'
    template_name = 'properties.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['main_posts'] = Posts.objects.all()[0:3]
        context['main_page'] = False
        return context



class PostDeleteView(DeleteView):
    model = Posts
    template_name='blog/posts_confirm_delete.html'
    success_url = reverse_lazy('user_page')
    context_object_name = 'post'


class PostChageView(UpdateView):
    model = Posts
    form_class = PostChageForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('user_page')
    context_object_name = 'post'


class DetailPageView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'property-details.html'

    def get_context_data(self, *args, **kwargs):
        author = Posts.objects.get(slug=self.kwargs.get('slug'))
        context = super().get_context_data()
        context['detail_pic'] = [i for i in range(3)]
        # context['main_page'] = False
        context['posts'] = Posts.objects.all()[0:3]
        if author.owner==self.request.user:
            context['is_author']=True
        else:
            context['is_author'] = False
        return context