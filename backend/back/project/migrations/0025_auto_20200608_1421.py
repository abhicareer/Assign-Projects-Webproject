# Generated by Django 3.0.2 on 2020-06-08 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_auto_20200608_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectactivity',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
