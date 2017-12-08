# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_log',
            field=models.FileField(upload_to=b''),
        ),
    ]
