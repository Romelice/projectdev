# Generated by Django 5.1.2 on 2025-01-17 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='date',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='messages',
        ),
    ]