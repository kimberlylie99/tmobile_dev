# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-26 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0008_auto_20190614_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autopage',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='bugpage',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='releasepage',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
