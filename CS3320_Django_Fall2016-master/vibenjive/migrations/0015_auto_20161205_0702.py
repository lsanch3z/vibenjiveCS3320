# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vibenjive', '0014_auto_20161205_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermusic',
            name='song_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
