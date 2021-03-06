# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 14:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_social'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name_plural': 'Social media links'},
        ),
        migrations.AddField(
            model_name='thing',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 14, 14, 51, 23, 323220, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thing',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 14, 14, 51, 39, 282937, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
