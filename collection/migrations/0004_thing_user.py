# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 14:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0003_auto_20160112_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
