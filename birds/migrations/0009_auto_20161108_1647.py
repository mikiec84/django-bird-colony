# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0008_auto_20161108_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='parents',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='parentz',
            new_name='parents'
        ),
    ]
