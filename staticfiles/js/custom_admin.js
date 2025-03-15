from django.contrib import admin
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'Custom Admin'
    site_title = 'Admin'
    index_title = 'Welcome to Custom Admin'

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'css/custom_admin.css'
        context['custom_js'] = 'js/custom_admin.js'
        return context

admin_site = CustomAdminSite()

@admin.register(SomeModel, site=admin_site)
class SomeModelAdmin(admin.ModelAdmin):
    pass
