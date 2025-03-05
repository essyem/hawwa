from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    due_date = models.DateField()

    def __str__(self):
        return self.name
