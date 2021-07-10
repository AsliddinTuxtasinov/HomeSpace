from django.urls import path
from main.views import HomePageView, BlogPageView, AboutPageView, ContactPageView, PropertiesPageView, DetailPageView

urlpatterns = [
    path('', HomePageView.as_view(),name='index'),
    path('blog/', BlogPageView.as_view(),name='blog'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('contact/', ContactPageView.as_view(),name='contact'),
    path('properties/', PropertiesPageView.as_view(),name='properties'),
    path('property-details/', DetailPageView.as_view(),name='property-details'),
]
