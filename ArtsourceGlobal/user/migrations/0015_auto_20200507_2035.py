# Generated by Django 2.2.4 on 2020-05-07 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20200507_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 20, 35, 0, 3747), verbose_name='sendTime'),
        ),
    ]
