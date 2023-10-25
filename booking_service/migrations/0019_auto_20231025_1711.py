# Generated by Django 3.2.22 on 2023-10-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_service', '0018_auto_20231025_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='special_request',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='special_requirments',
            field=models.TextField(default=''),
        ),
    ]
