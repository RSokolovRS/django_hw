# Generated by Django 5.0.3 on 2024-04-10 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_alter_student_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teachers',
        ),
    ]