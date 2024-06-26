# Generated by Django 3.2.22 on 2024-04-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_service', '0020_auto_20231027_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='special_request_requirments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=''),
        ),
    ]
