from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    # in theory, other form fields can be added here, but the 
    class meta:
        model = User
        fields = ['username', 'email' 'password1', 'password2']