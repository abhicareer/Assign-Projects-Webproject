# Generated by Django 2.2.5 on 2019-12-31 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageblock', '0004_imagelist_caption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagelist',
            old_name='image',
            new_name='user',
        ),
    ]
