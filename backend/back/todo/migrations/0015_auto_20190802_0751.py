# Generated by Django 2.2.3 on 2019-08-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_auto_20190802_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.AddField(
            model_name='todo',
            name='user_name',
            field=models.CharField(default='1', max_length=50),
        ),
    ]
