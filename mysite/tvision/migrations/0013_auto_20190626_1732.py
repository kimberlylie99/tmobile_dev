# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-26 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0012_auto_20190626_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autopage',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tvision.AutoLink'),
        ),
    ]
