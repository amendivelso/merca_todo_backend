# Generated by Django 3.2.8 on 2021-10-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_existing_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='existing_units',
            field=models.IntegerField(blank=True),
        ),
    ]