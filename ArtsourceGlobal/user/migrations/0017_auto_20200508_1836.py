# Generated by Django 2.2.4 on 2020-05-08 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20200508_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 18, 34, 34, 653631), verbose_name='sendTime'),
        ),
    ]