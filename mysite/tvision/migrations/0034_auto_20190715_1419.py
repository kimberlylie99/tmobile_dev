# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-15 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0033_delete_displayfrontimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='automatedpage',
            name='expected_results',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bugpage',
            name='expected_results',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='releasepage',
            name='expected_results',
            field=models.TextField(blank=True),
        ),
    ]
