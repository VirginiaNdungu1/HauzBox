# Generated by Django 2.0.1 on 2018-01-24 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Hauz', '0024_auto_20180124_0758'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Maintenance',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='house_id',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='house',
            name='occupancy',
        ),
        migrations.AddField(
            model_name='house',
            name='account_no',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='original_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_tenant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]