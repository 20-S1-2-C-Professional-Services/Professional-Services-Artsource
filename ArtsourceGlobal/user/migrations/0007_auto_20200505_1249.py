# Generated by Django 2.2.4 on 2020-05-05 02:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200505_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 12, 49, 40, 280892), verbose_name='sendTime'),
        ),
    ]
