# Generated by Django 3.0.2 on 2020-06-07 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_auto_20200607_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcreate',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 17, 31, 23, 181073)),
        ),
        migrations.AlterField(
            model_name='projectcreate',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 17, 31, 23, 181051)),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 17, 31, 23, 181611)),
        ),
    ]
