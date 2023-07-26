from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post
from .forms import AddPostForm

def feed(request):
    # Get all posts for now. TODO: Make posts only show for who you're following
    posts = Post.objects.all().order_by('-date')

    add_post_form = AddPostForm()
    return render(request, 'feed/feed.html', { 
            'posts': posts, 
            'add_post_form': add_post_form 
        })

@login_required
@require_POST
def add_post(request):
    form = AddPostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, 'You have successfully created your post')
    else:
        messages.error(request, 'There was a problem creating your post')
    return redirect(reverse('feed'))