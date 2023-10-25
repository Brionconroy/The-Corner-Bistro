from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Reservation(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, default='')
    last_name = models.CharField(max_length=50, blank=False, null=False, default='')
    naming_id = models.AutoField(primary_key=True)
    email = models.EmailField(default='')
    date_and_time = models.DateTimeField()
    number_of_guests = models.PositiveSmallIntegerField()
    special_request = models.TextField(default='')
    special_requirments = models.TextField(default='')

    class Meta:
        ordering = ["naming_id"]

    def __str__(self):
        return self.first_name + " " + self.last_name