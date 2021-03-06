# Generated by Django 3.0.2 on 2020-03-20 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20200319_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectactivity',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 33, 33, 1233)),
        ),
        migrations.AlterField(
            model_name='projectbugs',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='projectbugs',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 33, 33, 235)),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 33, 33, 2230)),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 33, 32, 999238)),
        ),
        migrations.AlterField(
            model_name='projectreport',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 33, 33, 1233)),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 33, 33, 235)),
        ),
    ]
