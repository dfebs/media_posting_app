from django import forms
from .models import Post, Comment

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'text']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']