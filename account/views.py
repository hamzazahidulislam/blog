from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def create_post(request):
    form = CreatePost()
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form
    }
    return render(request, 'account/create-post.htm', context)


@login_required
def user_dashboard(request):
    return render(request, 'account/dashboard.htm')


def user_signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user-login'))

    context = {
        'form': form
    }
    return render(request, 'account/register.htm', context)


def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('user-dashboard'))

    context = {
        'form': form,
    }
    return render(request, 'account/login.htm', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user-login'))