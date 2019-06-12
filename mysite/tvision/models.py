# -*- coding: utf-8 -*-
#import datetime
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import forms

import csv
from django.http import HttpResponse

# Create your models here.
class AutoPage(models.Model):
    pub_date = models.DateField('date published')
    title_text = models.CharField(max_length=1000)
    description_text = models.TextField(blank=True)
    upload = models.ImageField(upload_to='auto_images/', default='auto_images/')
    def __str__(self):
        return self.title_text

class ReleasePage(models.Model):
    pub_date = models.DateField('date published')
    title_text = models.CharField(max_length=200)
    description_text = models.TextField(blank=True)
    upload = models.ImageField(upload_to='release_images/', default='release_images/')
    def __str__(self):
        return self.title_text

class BugPage(models.Model):
    pub_date = models.DateField('date published')
    title_text = models.CharField(max_length=200)
    description_text = models.TextField(blank=True)
    upload = models.ImageField(upload_to='bug_images/', default='bug_images/')
    def __str__(self):
        return self.title_text

# uploading Images
class ImageUploadForm(forms.Form):
    """Image Upload Form"""
    image = forms.ImageField()

def image_tag(self):
