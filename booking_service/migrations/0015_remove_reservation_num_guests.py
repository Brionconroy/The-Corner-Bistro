# Generated by Django 3.2.22 on 2023-10-16 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_service', '0014_reservation_num_guests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='num_guests',
        ),
    ]
