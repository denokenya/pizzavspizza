# Generated by Django 3.1.7 on 2021-11-16 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_pizzeria_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzeria',
            name='phone_number',
        ),
    ]
