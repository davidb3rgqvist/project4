from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from recipe.models import Recipe
import logging

logger = logging.getLogger(__name__)


def register_view(request):
    """
    Let users to register as a user
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})


def login_view(request):
    """
    Let users access the page and create a cookbook
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_view')
    else:
        form = AuthenticationForm()

    reload_modal = bool(form.errors)
    return render(request, 'registration/login.html', locals())


def logout_view(request):
    """
    Let users logout from their cookbook.
    """
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
