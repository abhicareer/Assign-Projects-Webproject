# Generated by Django 2.2.5 on 2020-01-07 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20200107_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceadd',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useradd', to=settings.AUTH_USER_MODEL),
        ),
    ]
