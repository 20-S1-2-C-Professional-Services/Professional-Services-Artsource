# Generated by Django 2.2.4 on 2020-05-04 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200503_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 0, 38, 59, 997990), verbose_name='sendTime'),
        ),
    ]