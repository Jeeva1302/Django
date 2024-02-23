# Generated by Django 5.0 on 2024-01-08 12:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeedetails', '0002_employee_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Zipcode',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='streetadress',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
