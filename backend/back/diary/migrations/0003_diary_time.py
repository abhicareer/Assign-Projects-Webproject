# Generated by Django 2.2.5 on 2019-09-15 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20190915_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='time',
            field=models.TimeField(default=datetime.time),
        ),
    ]
