# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='price',
            field=models.IntegerField(default=10, max_length=10),
            preserve_default=False,
        ),
    ]
