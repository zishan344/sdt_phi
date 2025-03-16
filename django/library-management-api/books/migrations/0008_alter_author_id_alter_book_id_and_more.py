# Generated by Django 5.1.6 on 2025-03-16 09:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_author_id_alter_book_id_alter_borrowrecord_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.UUID('acd228ca-1c18-4b52-8056-d0d9cc60ba18'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.UUID('96be49ec-4cbc-405e-ae99-facdbbbec578'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='borrow_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2444a759-60f7-4c6e-881b-93d377f837dc'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7c0655c3-3436-4539-875c-4754c81daed4'), editable=False, primary_key=True, serialize=False),
        ),
    ]
