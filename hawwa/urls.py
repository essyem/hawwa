from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from .views import home, register, custom_admin_login
#from hawwa.admin import CustomAdminSite

# Custom admin sites
#custom_admin_site = CustomAdminSite()
#admin.site.register(User)  # Register User model in the default admin
#admin.site.register(TOTPDevice, TOTPDeviceAdmin)  # Register TOTPDevice in the default admin

urlpatterns = [
    # Public views
    path('', home, name='home'),
    path('register/', register, name='register'),
    #path('verify_totp/', verify_totp, name='verify_totp'),
    #path('verify-otp/', verify_otp, name='verify_otp'),
    #path('register_totp_device/', register_totp_device, name='register_totp_device'),

    # Admin sites
    path('custom-admin/login/', custom_admin_login, name='custom_admin_login'),  # Custom admin login
    #path('custom-admin/', custom_admin_site.urls, name='custom_admin'),  # Custom admin site
    path('admin/', admin.site.urls, name='default_admin'),  # Default admin site
    # Auth-related URLs
    path('accounts/', include('django.contrib.auth.urls')),
    #path('adminops/', include('adminops.urls')),

    # API endpoints
    path('api/vendors/', include('vendors.urls')),
    path('api/wellness/', include('wellness.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
