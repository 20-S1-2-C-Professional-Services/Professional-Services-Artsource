# Generated by Django 2.2.4 on 2020-05-07 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200507_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 14, 33, 23, 932536), verbose_name='sendTime'),
        ),
    ]
