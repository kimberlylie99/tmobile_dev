# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-10 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0027_auto_20190710_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automatedpage',
            name='document_link',
            field=models.FileField(blank=True, default='auto_documents/', null=True, upload_to='auto_documents/'),
        ),
    ]
