# Generated by Django 2.2.4 on 2020-05-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_reservation_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='duration',
            field=models.FloatField(default=0.0),
        ),
    ]
