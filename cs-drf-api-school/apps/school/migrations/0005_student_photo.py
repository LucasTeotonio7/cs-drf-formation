# Generated by Django 3.2.9 on 2022-11-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]