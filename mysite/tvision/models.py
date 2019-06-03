# -*- coding: utf-8 -*-
#import datetime
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Auto(models.Model):
    title_text = models.CharField(max_length=200)
    comment_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

class ReleasePage(models.Model):
    title_text = models.CharField(max_length=200)
    comment_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

class BugPage(models.Model):
    title_text = models.CharField(max_length=200)
    comment_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
