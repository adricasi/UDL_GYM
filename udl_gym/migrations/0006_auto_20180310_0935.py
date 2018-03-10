# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udl_gym', '0005_auto_20180308_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='gym',
        ),
        migrations.RemoveField(
            model_name='trainers',
            name='gym',
        ),
    ]
