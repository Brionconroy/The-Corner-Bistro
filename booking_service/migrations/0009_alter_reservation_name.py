# Generated by Django 3.2.22 on 2023-10-16 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_service', '0008_alter_reservation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
