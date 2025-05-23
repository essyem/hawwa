from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="hawwa_userprofile"  # Ensures a unique related_name
    )

    def __str__(self):
        return f"UserProfile for {self.user.username}"

# CustomUser model
class CustomUser(AbstractUser):
    # Additional fields
    department = models.ForeignKey(
        'adminops.Department',  # Reference to the Department model
        on_delete=models.SET_NULL,  # Allow null if the department is deleted
        null=True,
        blank=True
    )
    is_verified = models.BooleanField(default=False)  # Add the missing field

    def __str__(self):
        return self.username

# EmailOTP model
class EmailOTP(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Use the custom user model
        on_delete=models.CASCADE
    )
    otp = models.CharField(max_length=6)  # OTP code
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.user.username} created at {self.created_at}"

#class Sales(models.Model):

