# Generated by Django 4.2.2 on 2023-06-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_passengers_bookings_passengers_names_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='time_of_departure',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
