# Generated by Django 2.2.4 on 2020-05-07 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200507_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'artwork', 'verbose_name_plural': 'artworks'},
        ),
    ]
