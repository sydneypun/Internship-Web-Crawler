# Generated by Django 3.0 on 2019-12-13 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0005_auto_20191212_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='skills',
        ),
    ]