# Generated by Django 5.1.4 on 2025-03-08 11:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
