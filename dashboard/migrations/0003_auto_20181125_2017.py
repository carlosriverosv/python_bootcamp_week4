# Generated by Django 2.1.3 on 2018-11-25 20:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20181124_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='index',
        ),
    ]
