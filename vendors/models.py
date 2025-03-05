from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    room_types = models.JSONField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name
