from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from hawwa.models import CustomUser
from adminops.forms import UserCreationForm
from adminops.models import (
    Department, UserProfile, Expense, Revenue, Category, Tag, Attachment, Budget,
    Vendor, Invoice, Payment, Employee, Payroll, Tax, TaxApplication, Sales
)

# Register Department model
admin.site.register(Department)

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

# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Register Tag model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register Attachment model
@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')

# Register Expense model
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'date', 'category')
    filter_horizontal = ('tags', 'attachments')

# Register Revenue model
@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'date', 'category')
    filter_horizontal = ('tags', 'attachments')

# Register Budget model
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('department', 'amount', 'spent_amount', 'remaining_budget')
    readonly_fields = ('remaining_budget',)  # Make remaining_budget read-only


# Register Vendor model
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email')
    search_fields = ('name', 'contact', 'email')

# Register Invoice model
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'date', 'client', 'amount', 'vendor')
    search_fields = ('invoice_number', 'client', 'vendor__name')

# Register Payment model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'amount', 'date', 'payment_method')
    search_fields = ('invoice__invoice_number', 'payment_method')

# Register Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary')
    search_fields = ('name',)

# Register Payroll model
@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'salary', 'deductions', 'net_salary')
    readonly_fields = ('net_salary',)

    def net_salary(self, obj):
        return obj.net_salary
    net_salary.short_description = 'Net Salary'

# Register Tax model
@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate')
    search_fields = ('name',)

# Register TaxApplication model
@admin.register(TaxApplication)
class TaxApplicationAdmin(admin.ModelAdmin):
    list_display = ('tax', 'revenue', 'expense', 'amount')
    search_fields = ('tax__name', 'revenue__description', 'expense__description')
