from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import BasicRegistrationForm, UserRegistrationForm
import qrcode
import io
from django.contrib.auth.decorators import login_required
from django_otp.plugins.otp_totp.models import TOTPDevice

def home(request):
    return render(request, 'home.html', {'title': 'Welcome to Hawwa Wellness', 'subtitle': None})  # Add 'subtitle'

def register(request):
    if request.method == 'POST':
        form = BasicRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BasicRegistrationForm()
    return render(request, 'register.html', {'form': form, 'title': 'Register', 'subtitle': 'Create a new account'})

@csrf_protect
def custom_admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('admin:index')
                if hasattr(user, 'is_verified') and user.is_verified:
                    request.session['pre_otp_user_id'] = user.id
                    send_otp_via_email(user)
                    return redirect('verify_otp')
                else:
                    login(request, user)
                    return redirect('verify_totp')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'title': 'Admin Login',
        'subtitle': 'Login to Admin',
        'is_nav_sidebar_enabled': 'false'
    }
    return render(request, 'registration/login.html', context)

@login_required
def register_totp_device(request):
    user = request.user
    qr_code_data = None
    if request.method == 'POST':
        device = TOTPDevice.objects.create(user=user, name="Primary")
        totp_uri = device.config_url

        # Generate QR code
        qr = qrcode.make(totp_uri)
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)

        qr_code_data = buffer.getvalue()

    return render(request, 'registration/totp_registration.html', {
        'title': 'Register TOTP Device',
        'qr_code_data': qr_code_data,
        'subtitle': 'Secure your account with TOTP'
    })

@login_required
def verify_totp(request):
    if request.method == 'POST':
        user = request.user
        totp_code = request.POST.get('totp_code')
        device = TOTPDevice.objects.filter(user=user, name="Primary").first()

        if device and device.verify_token(totp_code):
            user.is_verified = True
            user.save()
            return redirect('home')
        else:
            return HttpResponse("Invalid TOTP code.")

    return render(request, 'registration/verify_totp.html', {'title': 'Verify TOTP Code', 'subtitle': 'Enter your TOTP code to verify'})

def verify_otp(request):
    # Your logic for verifying OTP
    return HttpResponse("OTP verified")
