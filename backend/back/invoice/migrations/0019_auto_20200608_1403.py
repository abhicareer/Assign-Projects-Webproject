# Generated by Django 3.0.2 on 2020-06-08 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0018_auto_20200607_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceprojectjoin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 14, 3, 8, 742804)),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 14, 3, 8, 743304)),
        ),
        migrations.AlterField(
            model_name='subs',
            name='txn_date',
            field=models.CharField(default=datetime.datetime(2020, 6, 8, 14, 3, 8, 743868), max_length=50),
        ),
    ]
