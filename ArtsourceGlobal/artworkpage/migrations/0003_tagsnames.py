# Generated by Django 2.2.4 on 2020-05-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworkpage', '0002_auto_20200425_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]
