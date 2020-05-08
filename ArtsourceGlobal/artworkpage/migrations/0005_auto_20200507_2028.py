# Generated by Django 2.2.4 on 2020-05-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworkpage', '0004_artwork_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_names', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='description',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AddField(
            model_name='artwork',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artwork',
            name='length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artwork',
            name='width',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='artwork',
            name='artists',
            field=models.ManyToManyField(related_name='created_artwork', to='artworkpage.ArtistNames'),
        ),
    ]