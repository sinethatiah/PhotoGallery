from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Photo, Tag, PhotoInteraction, Profile


def register(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('home')
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'registration/profile.html', {'form': form})


def home(request):
    tag = request.GET.get('tag')
    photos = Photo.objects.filter(tags__name=tag) if tag else Photo.objects.all()
    return render(request, 'home.html', {
        'photos': photos,
        'tags': Tag.objects.all(),
        'selected_tag': tag,
    })


@login_required
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo_detail.html', {
        'photo': photo,
        'like_count': photo.interactions.filter(interaction_type='like').count(),
        'dislike_count': photo.interactions.filter(interaction_type='dislike').count(),
        'user_interaction': PhotoInteraction.objects.filter(user=request.user, photo=photo).first(),
    })


@login_required
def toggle_interaction(request, pk, interaction_type):
    photo = get_object_or_404(Photo, pk=pk)
    existing = PhotoInteraction.objects.filter(user=request.user, photo=photo).first()

    if existing and existing.interaction_type == interaction_type:
        existing.delete()
    elif existing:
        existing.interaction_type = interaction_type
        existing.save()
    else:
        PhotoInteraction.objects.create(user=request.user, photo=photo, interaction_type=interaction_type)

    return redirect('photo_detail', pk=pk)
