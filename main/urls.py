from django.urls import path
from .views import (
    HomePageView,SubscribeView,AboutPageView,ContactPageView,# BlogPageView,
    PropertiesPageView,DetailPageView,PostCommentView,ContactWithAgentView,ContactWithAgentDeleteView
)

app_name='main'

urlpatterns = [
    path('', HomePageView.as_view(),name='index'),
    path('subscribe/', SubscribeView.as_view(),name='subscribe'),
    # path('blog/', BlogPageView.as_view(),name='blog'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('contact/', ContactPageView.as_view(),name='contact'),
    path('properties/', PropertiesPageView.as_view(), name='properties'),

    path('property/<slug:slug>/', DetailPageView.as_view(), name='property'),
    path('comment/<slug:slug>/', PostCommentView.as_view(), name='comment'),
    path('contact-with-agent/<slug:slug>/', ContactWithAgentView.as_view(), name='contact'),
    path('contact-with-agent-delete/<int:pk>/', ContactWithAgentDeleteView.as_view(), name='contact_delete'),
]
