from hawwa.models import CustomUser
from adminops.forms import UserCreationForm
from adminops.models import Department, UserProfile, Expense, Revenue, Report
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register Department model
admin.site.register(Department)

# Register Expense model
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'date')
    search_fields = ('category', 'description')

# Register Revenue model
@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount', 'date')
    search_fields = ('source', 'description')

# Register Report model
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'generated_on')
    search_fields = ('title',)

# Register UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_department')  # Display username and department
    search_fields = ('user__username', 'user__department__name')  # Search user details
    ordering = ('user__username',)
    actions = ['set_rbac_permissions', 'create_user']  # Add create_user action

    # Method to retrieve the department from CustomUser
    def get_department(self, obj):
        return obj.user.department
    get_department.short_description = 'Department'

    # Action to manage RBAC permissions
    def set_rbac_permissions(self, request, queryset):
        for userprofile in queryset:
            try:
                group = Group.objects.get(name="View Group")
                userprofile.user.user_permissions.add(*group.permissions.all())
            except Group.DoesNotExist:
                self.message_user(request, "View Group does not exist. Please create it first.", level="error")
        self.message_user(request, "RBAC permissions updated successfully!")

    # Custom action to create a new user
    def create_user(self, request, queryset):
        from django.shortcuts import render
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        from adminops.forms import UserCreationForm

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                self.message_user(request, f"User '{new_user.username}' created successfully.")
                return HttpResponseRedirect(reverse('admin:adminops_userprofile_changelist'))
        else:
            form = UserCreationForm()

        return render(request, 'admin/create_user.html', {'form': form})
    create_user.short_description = 'Create a new user'

# Register CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'department')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'department'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'department', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
