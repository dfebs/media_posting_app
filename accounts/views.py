from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from pathlib import Path

from .forms import RegistrationForm
from .models import UserProfile, User


def users(request):
    # TODO pass in values for list of users
    return render(request, 'accounts/users.html')

def profile(request, name):
    # TODO construct profile.html and pass in values
    user = get_object_or_404(User, username=name)
    profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'accounts/profile.html', {
        'username': user.username, 
        'profile': profile
        })

def log_out(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect(reverse('feed'))

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('feed:feed'))
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save() # TODO Verify this assignment isnt needed
            new_user = authenticate (
                username=request.POST['username'], 
                password=request.POST['password1']
            )
            login(request, new_user) # TODO create a user profile model on new register
            profile = UserProfile(
                user=new_user, 
                description="This is the default bio",
                picture=str(Path.joinpath(settings.MEDIA_ROOT, 'default/profile.png'))
                )
            profile.save()

            messages.success(request, 'You have successfully registered for the site.')

            return redirect(reverse('feed'))
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})