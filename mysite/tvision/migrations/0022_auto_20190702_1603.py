# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-02 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0021_auto_20190702_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autopage',
            old_name='precondition_text',
            new_name='precondition',
        ),
        migrations.RenameField(
            model_name='autopage',
            old_name='title_text',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='bugpage',
            old_name='precondition_text',
            new_name='precondition',
        ),
        migrations.RenameField(
            model_name='bugpage',
            old_name='title_text',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='releasepage',
            old_name='precondition_text',
            new_name='precondition',
        ),
        migrations.RenameField(
            model_name='releasepage',
            old_name='title_text',
            new_name='title',
        ),
    ]