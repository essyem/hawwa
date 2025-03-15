import random
from django.core.mail import send_mail
from .models import EmailOTP

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_via_email(user):
    otp = generate_otp()
    EmailOTP.objects.create(user=user, otp=otp)
    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp}',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )
