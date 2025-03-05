from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home, register

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('register/', register, name='register'),  # Registration
    # path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
    path('api/vendors/', include('vendors.urls')),
    path('api/wellness/', include('wellness.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





# Add error handlers (if not already present)
#handler404 = 'your_app.views.custom_404_view'  # Replace with your custom 404 view
#handler500 = 'your_app.views.custom_500_view'  # Replace with your custom 500 view
