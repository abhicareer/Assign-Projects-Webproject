# Generated by Django 3.0.2 on 2020-06-07 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20200326_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 7, 17, 16, 24, 865816)),
        ),
    ]