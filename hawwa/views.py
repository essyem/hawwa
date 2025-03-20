from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from .forms import BasicRegistrationForm

# Home view
def home(request):
    return render(request, 'home.html', {'title': 'Welcome to Hawwa Wellness'})

# Registration view
def register(request):
    if request.method == 'POST':
        form = BasicRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BasicRegistrationForm()
    return render(request, 'register.html', {'form': form, 'title': 'Register', 'subtitle': 'Create an Account'})

# Admin login view
@csrf_protect
def custom_admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin:index')
    else:
        form = AuthenticationForm()
    return render(request, 'admin/login.html', {'form': form, 'title': 'Admin Login', 'subtitle': 'Login to Admin'})
