# Generated by Django 3.0.4 on 2020-03-31 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_album_album_uri'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist_uri',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
