from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('profile/<username>', views.profile, name='profile'),
    path('users/', views.users, name='users'),
]