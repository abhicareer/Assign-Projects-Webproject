# Generated by Django 3.0.2 on 2020-02-07 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='parent',
            new_name='user',
        ),
    ]
