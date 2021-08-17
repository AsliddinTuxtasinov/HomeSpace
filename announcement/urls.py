from django.urls import path
from .views import PostCreateView, PostChageView,DetailPageView,PostDeleteView,PostCommentView,load_cities

urlpatterns = [
    path('create_post/', PostCreateView.as_view(), name='create_post'),
    path('post/<slug:slug>/', DetailPageView.as_view(), name='post-detail'),
    path('post/<slug:slug>/edit', PostChageView.as_view(), name='post-edit'),
    path('post/<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('comment/<slug:slug>/', PostCommentView.as_view(), name='comment'),

    path('ajax/load-cities/', load_cities,
         name='ajax_load_cities'), # AJAX
]
