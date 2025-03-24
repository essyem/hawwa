# vendors/models.py
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    room_types = models.JSONField()
    availability = models.BooleanField(default=True)
    amenities_inclusive = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class NursingProvider(models.Model):
    name = models.CharField(max_length=200)
    certifications = models.TextField()
    languages = models.JSONField()

    def __str__(self):
        return self.name

class CloudKitchen(models.Model):
    name = models.CharField(max_length=200)
    cuisine_type = models.CharField(max_length=100)  # E.g., Italian, Indian, etc.
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
