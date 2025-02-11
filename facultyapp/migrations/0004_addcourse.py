# Generated by Django 5.0.7 on 2024-10-07 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_task'),
        ('facultyapp', '0003_delete_addcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('AOOP', 'ADVANCED OBJECT ORIENTED PROGRAMMING'), ('PFSD', 'PYTHON FULL STACK DEVELOPMENT')], max_length=50)),
                ('section', models.CharField(choices=[('S11', 'SECTION S11'), ('S12', 'SECTION S12'), ('S13', 'SECTION S13'), ('S14', 'SECTION S14'), ('S15', 'SECTION S15'), ('S16', 'SECTION S16'), ('S17', 'SECTION S17')], max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentlist')),
            ],
        ),
    ]
