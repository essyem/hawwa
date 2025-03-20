from django import forms
from django.contrib.auth.models import Group
from hawwa.models import CustomUser
from adminops.models import Department

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    rbac_group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'department']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
