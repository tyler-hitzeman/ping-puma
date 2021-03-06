import datetime
from django.db import models
from django.utils import timezone


class Company(models.Model):
    company = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    timezone = models.CharField(max_length=200)

    def __str__(self):
        """returns a human-readable representation of the model"""
        return self.company


class Guest(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    reservation = models.CharField(max_length=500)
    email = models.EmailField()
    roomNumber = models.IntegerField()
    startTimestamp = models.DateTimeField('start time')
    endTimestamp = models.DateTimeField('end time')

    def __str__(self):
        """returns a human-readable representation of the model"""
        return self.lastName

    def update_field(self, key, value):
        getattr(self, key)
        setattr(self, key, value)

    def checked_in_within_last_24hrs(self):
        return self.checkin_time >= timezone.now - datetime.timedelta(days=1)


class Ping(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=5000)
    is_template = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, default=None)

    def __str__(self):
        """returns a human-readable representation of the model"""
        return self.subject
