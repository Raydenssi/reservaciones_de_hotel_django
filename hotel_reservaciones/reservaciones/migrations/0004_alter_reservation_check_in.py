# Generated by Django 5.0.6 on 2024-07-07 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
