# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import music.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('artist', models.CharField(max_length=200)),
                ('album_title', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=150)),
                ('album_log', models.CharField(max_length=1000)),
                ('repeat_song', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('city', models.CharField(default=music.models.default_city, max_length=30)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Active?')),
                ('file_type', models.CharField(max_length=1000)),
                ('size', models.CharField(max_length=1, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'P', b'Portion')])),
                ('album', models.ForeignKey(to='music.Album', db_index=False)),
            ],
        ),
    ]
