# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20171020_1423'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
