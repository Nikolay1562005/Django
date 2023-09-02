from django.urls import reverse_lazy
from .forms import CustomUserRegister
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegister(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password1')
            form.save()
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=password)
            login(request, user=user)
            return redirect(reverse('profile'))
        return render(request, 'app_auth/register.html', {'form': form})
    form = CustomUserRegister()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('profile'))
        return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('profile'))
    return redirect(reverse('app_auth/login.html', {'error': 'пользователь не найден'}))


@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))