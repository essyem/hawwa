from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from adminops.models import UserProfile
import random

class Command(BaseCommand):
    help = 'Creates 100 users with different roles'

    def handle(self, *args, **kwargs):
        roles = ['admin', 'manager', 'employee']
        for i in range(1, 101):
            username = f'user{i}'
            email = f'{username}@example.com'
            password = 'password123'  # Use a secure password in production
            role = random.choice(roles)

            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Create user profile
            profile = UserProfile(user=user, role=role)
            profile.save()

            self.stdout.write(self.style.SUCCESS(f'Created user {username} with role {role}'))
