# Generated by Django 3.2.8 on 2021-10-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_alter_providers_units_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providers',
            name='units_shipping',
            field=models.IntegerField(blank=True),
        ),
    ]
