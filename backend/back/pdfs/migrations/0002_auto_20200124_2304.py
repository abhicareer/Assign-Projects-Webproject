# Generated by Django 2.2.5 on 2020-01-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
