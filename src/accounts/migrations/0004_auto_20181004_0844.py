# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-04 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181004_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
