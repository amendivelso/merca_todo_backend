# Generated by Django 3.2.8 on 2021-10-12 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20211012_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providers',
            name='units_shipping',
            field=models.IntegerField(blank=True, max_length=11),
        ),
    ]
