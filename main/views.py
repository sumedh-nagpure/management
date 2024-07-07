# main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm, LoginForm, UserCreationForm
from .models import Organization

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email_domain = user.email.split('@')[1]
            try:
                organization = Organization.objects.get(email_domain=email_domain)
            except Organization.DoesNotExist:
                organization = Organization.objects.get(name='Global')
            user.organization = organization
            user.save()
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def create_user_view(request):
    if not request.user.is_staff:
        return render(request, 'main/admin_required.html')  # Render a template with a message

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.organization = Organization.objects.get(name='Global')
            user.save()
            return redirect('home')  # Redirect to admin user list or home page
    else:
        form = UserCreationForm()
    return render(request, 'main/create_user.html', {'form': form})
@login_required
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('home')  # Redirect to 'home' URL name
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'main/home.html')
