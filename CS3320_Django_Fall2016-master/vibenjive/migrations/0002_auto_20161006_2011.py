# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vibenjive', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VibenjiveUsers',
            new_name='VibenjiveUser',
        ),
    ]