# Generated by Django 2.1.4 on 2023-11-17 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20231117_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
    ]
