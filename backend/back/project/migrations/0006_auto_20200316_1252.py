# Generated by Django 3.0.2 on 2020-03-16 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20200316_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcreate',
            name='Status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='projectactivity',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 12, 52, 18, 841471)),
        ),
        migrations.AlterField(
            model_name='projectbugs',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 12, 52, 18, 841471)),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 12, 52, 18, 841471)),
        ),
        migrations.AlterField(
            model_name='projectreport',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 12, 52, 18, 841471)),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 16, 12, 52, 18, 841471)),
        ),
    ]
