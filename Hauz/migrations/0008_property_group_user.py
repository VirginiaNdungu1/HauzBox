# Generated by Django 2.0.1 on 2018-01-18 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Hauz', '0007_property_property_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_group',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_property_group', to=settings.AUTH_USER_MODEL),
        ),
    ]
