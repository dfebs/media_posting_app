from django.urls import path

from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('add_post/', views.add_post, name='add_post')
]