# Generated by Django 3.0.2 on 2020-03-20 21:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20200321_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectbugs',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='projecttask',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='projectactivity',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 37, 6, 660223)),
        ),
        migrations.AlterField(
            model_name='projectbugs',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 37, 6, 659226)),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 37, 6, 660223)),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 37, 6, 657231)),
        ),
        migrations.AlterField(
            model_name='projectreport',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 37, 6, 659226)),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 2, 37, 6, 658228)),
        ),
    ]
