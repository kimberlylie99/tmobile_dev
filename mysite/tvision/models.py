# -*- coding: utf-8 -*-
#import datetime
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import forms
from django.forms import ModelForm
from django.contrib import admin

import csv
from django.http import HttpResponse

# Create your models here.
class AutoLink(models.Model):
    link_title = models.CharField(max_length=500)
    user_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.link_title

class ReleaseLink(models.Model):
    link_title = models.CharField(max_length=500)
    user_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.link_title

class BugLink(models.Model):
    link_title = models.CharField(max_length=500)
    user_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.link_title

class AutoPage(models.Model):
    pub_date = models.DateTimeField('date published')
    title_text = models.CharField(max_length=1000)
    description_text = models.TextField(blank=True)
    upload = models.ImageField(upload_to='auto_images/', default='auto_images/')
    link = models.ForeignKey(AutoLink, blank=True, null=True)
    def __str__(self):
        return self.title_text

class ReleasePage(models.Model):
    pub_date = models.DateTimeField('date published')
    title_text = models.CharField(max_length=200)
    description_text = models.TextField(blank=True)
    upload = models.ImageField(upload_to='release_images/', default='release_images/')
    link = models.ForeignKey(ReleaseLink, blank=True, null=True)
    def __str__(self):
        return self.title_text

class BugPage(models.Model):
    pub_date = models.DateTimeField('date published')
    title_text = models.CharField(max_length=200)
    description_text = models.TextField(blank=True)
    upload = models.ImageField(upload_to='bug_images/', default='bug_images/')
    link = models.ForeignKey(BugLink, blank=True, null=True)
    def __str__(self):
        return self.title_text

# uploading Images
class ImageUploadForm(forms.Form):
    """Image Upload Form"""
    image = forms.ImageField(required=False)

# date filter
class StartDateForm(forms.Form):
    """Get User Input Date"""
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

class EndDateForm(forms.Form):
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
