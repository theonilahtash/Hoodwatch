# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 16:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0006_auto_20181021_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='join',
            old_name='hood',
            new_name='hood_id',
        ),
        migrations.RenameField(
            model_name='join',
            old_name='user',
            new_name='user_id',
        ),
    ]
