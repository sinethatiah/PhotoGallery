from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'gallery/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {'form': form})
