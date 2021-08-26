from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.http import Http404

from django.views.generic.base import TemplateView
from django.views.generic import ListView,CreateView
from django.views.generic.base import View

from django.contrib import messages
from django.core.mail import send_mail

from authusers.models import Agents,Founders
from announcement.models import Posts
from .models import Contact
from .forms import FilterHomeForm,SubscribeForm,ContactWithAgentForm,ContactForm



# Home page View
class HomePageView(ListView):
    queryset = Posts.objects.all()
    context_object_name = 'posts'
    template_name = 'index.html'
    paginate_by = 9
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset=FilterHomeForm(self.request.GET, queryset=queryset)
        return queryset.qs

    def get_context_data(self, *args, **kwargs):
        try:
            context = super().get_context_data()
        except Http404:
            self.kwargs['page'] = 1
            context = super().get_context_data()

        context['agents']       = Agents.objects.all()
        context['main_posts'] = Posts.objects.all()[0:3]
        context['subsribe_form'] =SubscribeForm
        context['main_page']  = True
        context['filter_form']=FilterHomeForm(self.request.GET, queryset = self.get_queryset())
        # for paginition
        context['region_page']         = ''.join([ f"region={x}&"for x in self.request.GET.getlist('region') ])
        context['district_page']       = ''.join([ f"district={x}&"for x in self.request.GET.getlist('district') ])
        context['home_type_page']      = ''.join([ f"home_type={x}&"for x in self.request.GET.getlist('home_type') ])
        context['type_page']           = ''.join([ f"type={x}&"for x in self.request.GET.getlist('type') ])
        context['price__lt_page']      = ''.join([ f"price__lt={x}&"for x in self.request.GET.getlist('price__lt') ])
        context['price__gt_page']      = ''.join([ f"price__gt={x}&"for x in self.request.GET.getlist('price__gt') ])
        context['area__lt_page']       = ''.join([ f"area__lt={x}&"for x in self.request.GET.getlist('area__lt') ])
        context['area__gt_page']       = ''.join([ f"area__gt={x}&"for x in self.request.GET.getlist('area__gt') ])
        context['year_build__lt_page'] = ''.join([ f"year_build__lt={x}&"for x in self.request.GET.getlist('year_build__lt') ])
        context['year_build__gt_page'] = ''.join([ f"year_build__gt={x}&"for x in self.request.GET.getlist('year_build__gt') ])
        return context


# Sbscribe View
class SubscribeView(CreateView):
    queryset = Posts
    form_class = SubscribeForm

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        try:
            email=request.POST['email']
            emails=SubscribeEmail.objects.get(email=email)
        except:
            emails=None

        if emails:
            messages.error(request, "Bu email obuna bo'lingan!")
            return redirect('/')
        else:
            if form.is_valid():
                form.save(commit=False)
                to=[form.cleaned_data.get('email')]

                try:
                    send_mail(
                        "Mufaqqiyatli obuna bo'lindi!",
                        "Mufaqqiyatli obuna bo'ldingiz, bu sizga eng so'ngi e'lonlardan habardor bo'lasiz!",
                        '',to,fail_silently=False,)
                except:
                    messages.error(request, "server bilan bog'liq xatolik iltimos boshqattan urinib ko'ring!")
                    return redirect('/')

                form.save()
                messages.success(request,"Mufaqqiyatli obuna bo'lindi!")
                return redirect('/')

        messages.error(request, "Mufaqqiyatli obuna bo'linmadi iltimos tekshirib qayta urinib ko'ring !")
        return redirect('/')


# Announcment Page View
class AnnouncmentPageView(ListView):
    queryset = Posts.objects.all()
    context_object_name = 'posts'
    template_name = 'properties.html'
    paginate_by = 9
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset=FilterHomeForm(self.request.GET, queryset=queryset)
        return queryset.qs

    def get_context_data(self, *args, **kwargs):
        try:
            context = super().get_context_data()
        except Http404:
            self.kwargs['page'] = 1
            context = super().get_context_data()

        context['main_posts'] = Posts.objects.all()[0:3]
        context['main_page'] = False
        context['filter_form'] = FilterHomeForm(self.request.GET, queryset=self.get_queryset())
        context['region_page'] = ''.join([f"region={x}&" for x in self.request.GET.getlist('region')])
        context['district_page'] = ''.join([f"district={x}&" for x in self.request.GET.getlist('district')])
        return context


# About page View
class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['agents']  = Agents.objects.all()
        context['founders'] = Founders.objects.all()
        return context


# Contact Page View
class ContactPageView(CreateView):
    model=Contact
    form_class=ContactForm
    template_name ='contact.html'
    success_url = reverse_lazy('main:contact')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['agents'] = Agents.objects.all()
        context['contact_form'] = self.form_class
        return context
    
    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        self.object = form.save()
        messages.success(self.request,"Xabaringiz muoffiqiyatli yetkazildi!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, "Iltimos boshqattan urinib ko'ring bazi xotolar aniqlandi!")
        return self.render_to_response(self.get_context_data(form=form))



# Contact with Agent 
class ContactWithAgentView(View):
    model = Posts
    form_class = ContactWithAgentForm
    template_name = 'property-details.html'

    def get(self, request,slug):
        post = self.model.objects.get(slug=slug)
        messages.error(request, "iltimos boshqattan urinib ko'ring bazi xotolar aniqlandi!")
        return redirect(post.get_absolute_url())

    def post(self,request,slug):

        post=self.model.objects.get(slug=slug)
        contact_with_agent_form=self.form_class(request.POST)

        if contact_with_agent_form.is_valid():
            obj=contact_with_agent_form.save(commit=False)
            obj.post=post
            obj.agent=post.diller
            obj.save()
            messages.success(request,"xabaringiz agentga yetkazildi!")
            return redirect(post.get_absolute_url())
        messages.error(request, "iltimos boshqattan urinib ko'ring bazi xotolar aniqlandi!")
        return redirect(post.get_absolute_url())