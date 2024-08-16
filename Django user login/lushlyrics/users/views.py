# Create your views here.

# lushlyrics/users/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('thank_you')  # Changed to redirect to thank_you page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'users/home.html')

def registration_confirmation(request):
   return render(request, 'users/registration_confirmation.html')

def thank_you(request):
    return render(request, 'users/thank_you.html')


