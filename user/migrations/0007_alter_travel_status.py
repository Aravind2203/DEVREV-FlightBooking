# Generated by Django 4.2.2 on 2023-06-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_flight_time_of_departure_alter_travel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='status',
            field=models.CharField(default='active', max_length=10),
        ),
    ]
