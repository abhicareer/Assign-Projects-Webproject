# Generated by Django 2.2.3 on 2019-08-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20190802_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user_name',
        ),
        migrations.AddField(
            model_name='todo',
            name='username',
            field=models.CharField(default='1', max_length=50),
        ),
    ]
