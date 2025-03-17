from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create test users'

    def handle(self, *args, **kwargs):
        for i in range(1, 51):
            username = f'testuser{i}'
            email = f'testuser{i}@example.com'
            password = 'testpassword'
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)
        self.stdout.write("50 test users created successfully!")
