from django.shortcuts import render,redirect
from django.http import Http404,HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView,CreateView,View

from .models import Posts
from .forms import ContactWithAgentForm

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
        client=self.request.user
        agent=False
        if client.is_authenticated:
            agent=client.is_agent
        owner = self.object.owner == client

        context = super().get_context_data()
        context['detail_pic'] = [i for i in range(3)]
        # context['main_page'] = False
        context['posts'] = self.model.objects.all()[0:3]
        context['contact_with_agent_form'] = ContactWithAgentForm

        if agent or owner:
            context['is_author_or_agent']=True
        else:
            context['is_author_or_agent'] = False
        return context

# class ContactWithAgentView(CreateView):
#     # model = Posts
#     form_class = ContactWithAgentForm
#     template_name = 'property-details.html'
#
#     def get_queryset(self,slug):
#         queryset = Posts.objects.get(slug=slug)
#         # print(queryset)
#         # print("====",self.slug_field)
#         return queryset
#
#     def form_valid(self, form):
#         # post=self.model. # Posts.objects.get(slug=self.slug_field)
#         self.object = form.save(commit=False)
#         form.instance.post = self.model
#         form.instance.agent = self.model.diller
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         # kwargs = {'slug': self.slug_field}
#         # return reverse('main:property', kwargs=kwargs)
#         return self.model

class ContactWithAgentView(View):
    model = Posts
    form_class = ContactWithAgentForm
    template_name = 'property-details.html'

    def get(self, request,slug):
        context={
            'post':self.model.objects.get(slug=slug),
            'posts': self.model.objects.all()[0:3],
            'contact_with_agent_form':self.form_class
        }
        return render(request,self.template_name,context)

    def post(self,request,slug):

        post=self.model.objects.get(slug=slug)
        contact_with_agent_form=self.form_class(request.POST)

        if contact_with_agent_form.is_valid():
            obj=contact_with_agent_form.save(commit=False)
            obj.post=post
            obj.agent=post.diller
            obj.save()
            return redirect(post.get_absolute_url())
        context = {
            'post': self.model.objects.get(slug=slug),
            'posts': self.model.objects.all()[0:3],
            'contact_with_agent_form': self.form_class
        }
        return render(request, self.template_name, context)




# class BlogPageView(TemplateView):
#     template_name = 'blog.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data()
#         context['objs'] = [i for i in range(9)]
#         context['our_blog'] = [i for i in range(6)]
#         return context