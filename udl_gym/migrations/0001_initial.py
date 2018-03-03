# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('street', models.TextField(null=True, blank=True)),
                ('telephone', models.IntegerField(null=True, blank=True)),
                ('city', models.TextField(null=True, blank=True)),
                ('state_or_province', models.TextField(null=True, blank=True)),
                ('country', models.TextField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('street', models.TextField(null=True, blank=True)),
                ('telephone', models.IntegerField(null=True, blank=True)),
                ('city', models.TextField(null=True, blank=True)),
                ('state_or_province', models.TextField(null=True, blank=True)),
                ('country', models.TextField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('specialized', models.TextField(null=True, blank=True)),
                ('gym', models.ForeignKey(related_name='trainers', to='udl_gym.Gym', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='gym',
            field=models.ForeignKey(related_name='activities', to='udl_gym.Gym', null=True),
        ),
    ]
