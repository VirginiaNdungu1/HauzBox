# Generated by Django 2.0.1 on 2018-01-25 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hauz', '0027_payment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='name',
            new_name='tenant_name',
        ),
    ]
