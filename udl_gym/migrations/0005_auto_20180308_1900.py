# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udl_gym', '0004_trainers_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='date',
        ),
        migrations.RemoveField(
            model_name='trainers',
            name='date',
        ),
    ]
