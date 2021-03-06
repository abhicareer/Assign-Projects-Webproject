# Generated by Django 3.0.2 on 2020-03-18 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20200317_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectreport',
            old_name='requested_to',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='projectreport',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='projectactivity',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 17, 28, 27, 131097)),
        ),
        migrations.AlterField(
            model_name='projectbugs',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 17, 28, 27, 130099)),
        ),
        migrations.AlterField(
            model_name='projectbugs',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 17, 28, 27, 130099)),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 17, 28, 27, 131097)),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 17, 28, 27, 129102)),
        ),
        migrations.AlterField(
            model_name='projectreport',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 17, 28, 27, 130099)),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 17, 28, 27, 129102)),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 18, 17, 28, 27, 129102)),
        ),
    ]
