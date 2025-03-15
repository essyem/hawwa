from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class BasicRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'User ID'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        }

    mobile_number = forms.CharField(max_length=15, required=True)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
