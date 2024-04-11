# Generated by Django 5.0.3 on 2024-04-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_remove_student_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', through='school.Enrollment', to='school.teacher'),
        ),
    ]