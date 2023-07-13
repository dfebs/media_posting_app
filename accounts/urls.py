from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('log_out', views.log_out, name='log_out'),
    path('register/', views.register, name='register'),
    path('profile/<username>/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
]