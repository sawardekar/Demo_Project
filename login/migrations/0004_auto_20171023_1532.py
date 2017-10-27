# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20171020_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
