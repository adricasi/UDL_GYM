# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('udl_gym', '0003_remove_gym_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainers',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
