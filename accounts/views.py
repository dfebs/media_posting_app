from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegistrationForm

# Create your views here.
def users(request):
    # TODO pass in values for list of users
    return render(request, 'accounts/users.html')

def profile(request, username):
    # TODO construct profile.html and pass in values
    return render(request, 'accounts/profile.html', {'username': username})

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
            new_user = form.save()
            new_user = authenticate (
                username=request.POST['username'], 
                password=request.POST['password1']
            )
            login(request, new_user)

            messages.success(request, 'You have successfully registered for the site.')
            return redirect(reverse('feed'))
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})