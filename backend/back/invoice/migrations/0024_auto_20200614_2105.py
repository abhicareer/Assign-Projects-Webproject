# Generated by Django 2.2.13 on 2020-06-14 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0023_auto_20200614_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceprojectjoin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 14, 21, 5, 17, 329494)),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 14, 21, 5, 17, 329881)),
        ),
        migrations.AlterField(
            model_name='subs',
            name='txn_date',
            field=models.CharField(default=datetime.datetime(2020, 6, 14, 21, 5, 17, 330332), max_length=50),
        ),
    ]
