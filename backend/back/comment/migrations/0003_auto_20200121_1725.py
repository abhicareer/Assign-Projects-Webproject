# Generated by Django 2.2.5 on 2020-01-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20200120_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.CharField(default='/default/download_1.jpeg', max_length=500),
        ),
    ]
