# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-29 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibenjive', '0005_vibenjiveuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='vibenjiveuser',
            name='link',
            field=models.CharField(blank=True, max_length=210, null=True),
        ),
    ]
