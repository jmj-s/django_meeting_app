# Generated by Django 4.2.3 on 2023-07-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('floor', models.IntegerField(default=1)),
                ('room_number', models.IntegerField(default=1)),
            ],
        ),
    ]
