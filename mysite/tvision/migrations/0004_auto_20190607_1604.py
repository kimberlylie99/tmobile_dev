# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-07 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0003_auto_20190607_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autopage',
            name='comment_text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='autopage',
            name='title_text',
            field=models.CharField(max_length=1000),
        ),
    ]
