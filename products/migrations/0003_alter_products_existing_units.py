# Generated by Django 3.2.8 on 2021-10-12 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='existing_units',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
