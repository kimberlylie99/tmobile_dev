# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-27 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0016_auto_20190627_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autopage',
            old_name='title',
            new_name='title_text',
        ),
        migrations.RenameField(
            model_name='bugpage',
            old_name='title',
            new_name='title_text',
        ),
        migrations.RenameField(
            model_name='releasepage',
            old_name='title',
            new_name='title_text',
        ),
    ]
