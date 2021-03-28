# Generated by Django 2.2.3 on 2019-08-03 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0015_auto_20190802_0751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user_name',
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]