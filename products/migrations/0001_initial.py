# Generated by Django 3.2.8 on 2021-10-11 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=20)),
                ('existing_units', models.CharField(blank=True, max_length=11)),
                ('date_entry', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(max_length=20)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.providers')),
            ],
        ),
    ]
