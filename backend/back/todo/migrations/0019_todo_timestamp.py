# Generated by Django 3.0.2 on 2020-02-25 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_auto_20190803_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]