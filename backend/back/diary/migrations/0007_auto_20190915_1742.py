# Generated by Django 2.2.5 on 2019-09-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_auto_20190915_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='time',
        ),
        migrations.AlterField(
            model_name='diary',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
