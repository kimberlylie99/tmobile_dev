# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-11 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0028_auto_20190710_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automatedpage',
            name='document_link',
        ),
        migrations.RemoveField(
            model_name='bugpage',
            name='document_link',
        ),
        migrations.RemoveField(
            model_name='releasepage',
            name='document_link',
        ),
    ]
