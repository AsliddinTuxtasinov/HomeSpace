from django.urls import path
from .views import (
    HomePageView,SubscribeView,AboutPageView,ContactPageView,
    AnnouncmentPageView,ContactWithAgentView
)

app_name='main'

urlpatterns = [
    path('', HomePageView.as_view(),name='index'),
    path('subscribe/', SubscribeView.as_view(),name='subscribe'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('contact/', ContactPageView.as_view(),name='contact'),
    path('announcement/', AnnouncmentPageView.as_view(), name='announcement'),

    path('contact-with-agent/<slug:slug>/', ContactWithAgentView.as_view(), name='contact'), # ariza qoldirish uchun

]
