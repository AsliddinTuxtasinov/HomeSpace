from django.shortcuts import render, redirect  # second way for create post
from django.urls import reverse_lazy

from django.views.generic import ListView,CreateView,View,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()

from .forms import CostumeUserCreateForm,CostumeUserChangeForm,AgentsEditForm
from main.models import ContactWithAgent,SubscribeEmail
from announcement.models import Posts
from .models import Agents



# Sign up view
class SignUpView(CreateView):
    form_class = CostumeUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


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
            try:
                diller=Agents.objects.get(agent=client)
                queryset = self.model._default_manager.filter(diller=diller)
            except:
                queryset = self.model._default_manager.none()
        else:
            queryset = self.model._default_manager.filter(owner=client)
        return queryset
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        client = self.request.user
        if client.is_agent:
            context['contact_with_cilent_count']=len(ContactWithAgent.objects.filter(agent__agent=client))
        return context


# Contact With Client View
class ContactsListView(LoginRequiredMixin,ListView):
    model = ContactWithAgent
    context_object_name = 'contacts'
    template_name = 'profilePage/contact_with_client.html'
    paginate_by = 4

    def get_queryset(self):
        client = self.request.user
        if client.is_authenticated:
            try:
                diller=Agents.objects.get(agent=client)
                queryset = self.model._default_manager.filter(agent=diller)
            except:
                queryset = self.model._default_manager.none()
            return queryset
        return None

# Delete contact with agent leters
class ContactDeleteView(LoginRequiredMixin,DeleteView):
    model = ContactWithAgent
    success_url = reverse_lazy('contact-with-client-page')