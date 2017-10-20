# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='name',
            new_name='user_id',
        ),
    ]
