from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Ensure you're importing the correct model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser  # Ensure this is your custom user model
        fields = ['username', 'email', 'password1', 'password2']

