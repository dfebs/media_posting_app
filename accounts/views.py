from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, ProfileForm
from .models import UserProfile, User, UserFollowing


def users(request):
    profiles = UserProfile.objects.all()
    return render(request, 'accounts/users.html', {'profiles': profiles})

def profile(request, name):
    # TODO construct profile.html and pass in values
    user = get_object_or_404(User, username=name)
    profile = get_object_or_404(UserProfile, user=user)
    viewing_username = request.user.username

    try:
        follow_relationship = UserFollowing.objects.get(
            follower=profile.user, 
            following=request.user
        )
    except UserFollowing.DoesNotExist:
        follow_relationship = None

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'viewing_username': viewing_username,
        'follow_relationship': follow_relationship
        })

@login_required
def edit_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid(): # TODO enforce image sizes
            profile_to_edit = form.save(commit=False)
            profile_to_edit.user = request.user
            profile_to_edit.save()
            return redirect(reverse('profile', kwargs={ 
                'name': request.user.username 
            }))
    else:
        form = ProfileForm(instance=user_profile)
    
    return render(request, 'accounts/edit_profile.html', { 'form': form })


def log_out(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect(reverse('feed'))

def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, pk=user_id)
    user_following = UserFollowing(following=request.user, follower=user_to_follow)
    user_following.save()
    messages.success(request, f'You now follow { user_to_follow.username }')
    return redirect(reverse('profile', kwargs={ 
        'name': user_to_follow.username 
    }))
    # TODO consider fail cases here. simple redirect and message for trying to re-follow
    # TODO Make sure users can't follow themselves

def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, pk=user_id)
    user_relationship = get_object_or_404(UserFollowing, 
                                            follower=user_to_unfollow, 
                                            following=request.user)
    user_relationship.delete()
    messages.success(request, f'You have stopped following {user_to_unfollow.username}')
    return redirect(reverse('profile', kwargs={
        'name':user_to_unfollow.username
    }))

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('feed'))
    
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
                description='This is the default bio',
                picture='pfp/default/profile.png'
                )
            profile.save()

            messages.success(request, 'You have successfully registered for the site.')

            return redirect(reverse('feed'))
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})