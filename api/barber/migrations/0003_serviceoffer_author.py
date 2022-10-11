# Generated by Django 4.0.2 on 2022-02-15 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barber', '0002_alter_serviceunavailability_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceoffer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
