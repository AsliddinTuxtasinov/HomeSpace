from django.urls import path
from .views import (
    HomePageView,AboutPageView,ContactPageView,# BlogPageView,
    PropertiesPageView,DetailPageView
)

app_name='main'

urlpatterns = [
    path('', HomePageView.as_view(),name='index'),
    # path('blog/', BlogPageView.as_view(),name='blog'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('contact/', ContactPageView.as_view(),name='contact'),
    path('properties/', PropertiesPageView.as_view(), name='properties'),

    path('property/<slug:slug>/', DetailPageView.as_view(), name='property'),
]
