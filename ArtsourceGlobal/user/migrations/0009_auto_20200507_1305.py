# Generated by Django 2.2.4 on 2020-05-07 03:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200505_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 13, 5, 11, 92577), verbose_name='sendTime'),
        ),
    ]
