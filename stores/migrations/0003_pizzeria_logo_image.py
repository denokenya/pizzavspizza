# Generated by Django 3.1.7 on 2021-11-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20211116_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzeria',
            name='logo_image',
            field=models.ImageField(blank=True, default='pizzariaImages/pizzalogo.png', upload_to='pizzariaImages'),
        ),
    ]
