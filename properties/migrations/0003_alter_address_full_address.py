# Generated by Django 4.2.16 on 2025-04-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_address_full_address_alter_address_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='full_address',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
