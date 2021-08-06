from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    SignUpView, UserEditView ,UserPageView, PostCreateView,
    PostChageView, PostDeleteView,ContactWithClientView,load_cities

)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html'
    )),

    path('user_page/', UserPageView.as_view(), name='user_page'),
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('contact-with-client/', ContactWithClientView.as_view(), name='contact-with-client'), # contqct with client
    path('property/<slug:slug>/edit', PostChageView.as_view(), name='property-edit'),
    path('property/<slug:slug>/delete', PostDeleteView.as_view(), name='property-delete'),

    path('ajax/load-cities/', load_cities,
         name='ajax_load_cities'), # AJAX

]
