from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from django import forms 
# TODO get email to be required

User = get_user_model()

class RegistrationForm(UserCreationForm):
    # in theory, other form fields can be added here
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']