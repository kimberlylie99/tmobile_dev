# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-27 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0017_auto_20190627_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autopage',
            name='title_text',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
