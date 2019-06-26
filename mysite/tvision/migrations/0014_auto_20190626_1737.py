# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-26 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tvision', '0013_auto_20190626_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=500)),
                ('user_link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_title', models.CharField(max_length=500)),
                ('user_link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='bugpage',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tvision.BugLink'),
        ),
        migrations.AddField(
            model_name='releasepage',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tvision.ReleaseLink'),
        ),
    ]
