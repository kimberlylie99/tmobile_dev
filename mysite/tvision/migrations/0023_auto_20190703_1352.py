# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-03 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0022_auto_20190702_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autopage',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
