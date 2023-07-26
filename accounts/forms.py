from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms 

from .models import UserProfile
# TODO get email to be required

User = get_user_model()

class RegistrationForm(UserCreationForm):
    # in theory, other form fields can be added here
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['description', 'picture']