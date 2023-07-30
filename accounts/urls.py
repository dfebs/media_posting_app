from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('log_out', views.log_out, name='log_out'),
    path('register/', views.register, name='register'),
    path('users/<name>/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
    path('follow_user/<user_id>/', views.follow_user, name='follow_user'),
    path('unfollow_user/<user_id>/', views.unfollow_user, name='unfollow_user'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
]