# Generated by Django 2.2.5 on 2019-09-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_diary_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='posted_date',
        ),
        migrations.AlterField(
            model_name='diary',
            name='time',
            field=models.DateTimeField(default='2019-09-15 17:09'),
        ),
    ]
