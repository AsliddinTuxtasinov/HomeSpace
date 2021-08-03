from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import Posts


class HomePageView(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'index.html'
    paginate_by = 9
    paginate_orphans = 3

    def get_context_data(self, *args, **kwargs):
        try:
            context = super().get_context_data()
        except Http404:
            self.kwargs['page'] = 1
            context = super().get_context_data()


        context['objs']       = [i for i in range(9)]
        context['our_blog']   = [i for i in range(3)]
        context['main_posts'] = Posts.objects.all()[0:3]
        context['main_page']  = True
        return context


class PropertiesPageView(ListView):
    model=Posts
    context_object_name = 'posts'
    template_name = 'properties.html'
    paginate_by = 9
    paginate_orphans = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['main_posts'] = Posts.objects.all()[0:3]
        context['main_page'] = False
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
        context['agents'] = [i for i in range(9)]
        # context['leaders'] = [200,300,400,400,200,300]
        return context


class DetailPageView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'property-details.html'

    def get_context_data(self, *args, **kwargs):
        author = self.model.objects.get(slug=self.kwargs.get('slug'))
        context = super().get_context_data()
        context['detail_pic'] = [i for i in range(3)]
        # context['main_page'] = False
        context['posts'] = self.model.objects.all()[0:3]

        if author.owner==self.request.user:
            context['is_author']=True
        else:
            context['is_author'] = False
        return context


# class BlogPageView(TemplateView):
#     template_name = 'blog.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data()
#         context['objs'] = [i for i in range(9)]
#         context['our_blog'] = [i for i in range(6)]
#         return context