from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from .views import home, register, verify_totp, custom_admin_login, register_totp_device, verify_otp

class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('verify_totp/', verify_totp, name='verify_totp'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('register_totp_device/', register_totp_device, name='register_totp_device'),
    path('admin/login/', custom_admin_login, name='custom_admin_login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/vendors/', include('vendors.urls')),
    path('api/wellness/', include('wellness.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
