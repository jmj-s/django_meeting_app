# Generated by Django 4.2.3 on 2023-07-06 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='room',
        ),
    ]
