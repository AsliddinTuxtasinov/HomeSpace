from django.urls import path
from main.views import (
    HomePageView, BlogPageView, AboutPageView,ContactPageView,
    PropertiesPageView, DetailPageView, PostChageView, PostDeleteView
)

app_name='main'

urlpatterns = [
    path('', HomePageView.as_view(),name='index'),
    path('blog/', BlogPageView.as_view(),name='blog'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('contact/', ContactPageView.as_view(),name='contact'),
    path('properties/', PropertiesPageView.as_view(), name='properties'),

    path('property/<slug:slug>/', DetailPageView.as_view(), name='property'),
    path('property/<slug:slug>/edit', PostChageView.as_view(), name='property-edit'),
    path('property/<slug:slug>/delete', PostDeleteView.as_view(), name='property-delete'),
]
