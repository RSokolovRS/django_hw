# Generated by Django 4.2.7 on 2024-01-31 19:36

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_name_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=True, max_length=255, populate_from='name'),
        ),
    ]