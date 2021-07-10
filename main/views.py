from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views import View


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['objs'] = [i for i in range(9)]
        context['our_blog'] = [i for i in range(3)]
        context['posts'] = [i for i in range(6)]
        context['main_posts'] = [i for i in range(2)]
        context['main_page'] = True
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

class PropertiesPageView(TemplateView):
    template_name = 'properties.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['main_posts'] = [i for i in range(2)]
        context['main_page'] = False
        context['posts'] = [i for i in range(6)]
        return context


class DetailPageView(TemplateView):
    template_name = 'property-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['detail_pic'] = [i for i in range(3)]
        # context['main_page'] = False
        context['posts'] = [i for i in range(3)]
        return context