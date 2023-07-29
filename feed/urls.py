from django.urls import path

from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/<post_id>/', views.add_comment, name='add_comment'),
    path('delete_post/<post_id>/', views.delete_post, name='delete_post')
]