# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-26 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0011_auto_20190626_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autolink',
            old_name='link',
            new_name='user_link',
        ),
    ]
