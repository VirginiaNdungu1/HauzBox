# Generated by Django 2.0.1 on 2018-01-18 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hauz', '0009_auto_20180118_1705'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='amenity',
            table='amenity',
        ),
        migrations.AlterModelTable(
            name='expense',
            table='expense',
        ),
        migrations.AlterModelTable(
            name='house',
            table='houses',
        ),
        migrations.AlterModelTable(
            name='maintenance',
            table='maintenance',
        ),
        migrations.AlterModelTable(
            name='payment',
            table='payment',
        ),
        migrations.AlterModelTable(
            name='property_group',
            table='property_group',
        ),
        migrations.AlterModelTable(
            name='property_type',
            table='property_type',
        ),
        migrations.AlterModelTable(
            name='tenant',
            table='tenant',
        ),
    ]
