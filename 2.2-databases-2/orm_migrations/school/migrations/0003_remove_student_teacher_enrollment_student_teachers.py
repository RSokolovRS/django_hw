# Generated by Django 5.0.3 on 2024-04-20 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_group_alter_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.student')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='school.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='students', through='school.Enrollment', to='school.teacher'),
        ),
    ]