# Generated by Django 2.2.13 on 2020-06-14 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0022_auto_20200611_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceprojectjoin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 14, 19, 16, 51, 344970)),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 14, 19, 16, 51, 345335)),
        ),
        migrations.AlterField(
            model_name='subs',
            name='txn_date',
            field=models.CharField(default=datetime.datetime(2020, 6, 14, 19, 16, 51, 345676), max_length=50),
        ),
    ]
