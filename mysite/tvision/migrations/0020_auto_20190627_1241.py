# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-27 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0019_auto_20190627_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autopage',
            name='title_text',
            field=models.CharField(blank=True, default='BLANK', max_length=1000, null=True),
        ),
    ]
