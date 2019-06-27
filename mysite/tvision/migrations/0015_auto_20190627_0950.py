# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-27 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0014_auto_20190626_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autopage',
            name='upload',
            field=models.ImageField(blank=True, default='auto_images/', null=True, upload_to='auto_images/'),
        ),
        migrations.AlterField(
            model_name='bugpage',
            name='upload',
            field=models.ImageField(blank=True, default='bug_images/', null=True, upload_to='bug_images/'),
        ),
        migrations.AlterField(
            model_name='releasepage',
            name='upload',
            field=models.ImageField(blank=True, default='release_images/', null=True, upload_to='release_images/'),
        ),
    ]
