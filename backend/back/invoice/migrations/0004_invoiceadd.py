# Generated by Django 2.2.5 on 2020-01-06 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoice', '0003_delete_invoiceadd'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.CharField(default=' Invoice', max_length=60)),
                ('requested_by', models.IntegerField(default=-1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useradd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
