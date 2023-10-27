from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import django.utils.timezone


class Reservation(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, default='')
    last_name = models.CharField(max_length=50, blank=False, null=False, default='')
    naming_id = models.AutoField(primary_key=True)
    email = models.EmailField(default='')
    date = models.DateField(auto_now=False, default=django.utils.timezone.now)
    time = models.TimeField(default="12:00")
    number_of_guests = models.PositiveSmallIntegerField()
    special_request_requirments = models.TextField(default='')

    class Meta:
        ordering = ["naming_id"]

    def __str__(self):
        return self.first_name + " " + self.last_name
