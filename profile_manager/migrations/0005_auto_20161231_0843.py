# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-31 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_manager', '0004_auto_20161231_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='diff_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='provider',
            name='diff_flag',
            field=models.BooleanField(default=False),
        ),
    ]
