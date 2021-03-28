# Generated by Django 3.0.2 on 2020-03-20 11:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_profile_team_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(default='/default/profile-bg.jpg', upload_to='profile_bg_image'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('message_by', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 3, 20, 16, 50, 20, 119319))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
