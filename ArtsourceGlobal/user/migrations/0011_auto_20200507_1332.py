# Generated by Django 2.2.4 on 2020-05-07 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20200507_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 13, 32, 1, 100744), verbose_name='sendTime'),
        ),
    ]
