# Generated by Django 3.0.7 on 2024-11-14 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0007_auto_20241114_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='matric_number',
            new_name='matric_no',
        ),
    ]
