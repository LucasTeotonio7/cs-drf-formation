# Generated by Django 3.2.9 on 2022-10-08 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id'], 'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
    ]
