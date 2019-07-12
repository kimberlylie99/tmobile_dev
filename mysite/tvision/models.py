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

from django.core.files.storage import FileSystemStorage

# Including links
class AutomatedLink(models.Model):
    link_title = models.CharField(max_length=500, null=True)
    link_author = models.CharField(max_length=500, null=True)
    user_link = models.CharField(max_length=1000)
    def __str__(self):
        return self.link_title

class ReleaseLink(models.Model):
    link_title = models.CharField(max_length=500, null=True)
    link_author = models.CharField(max_length=500, null=True)
    user_link = models.CharField(max_length=1000)
    def __str__(self):
        return self.link_title

class BugLink(models.Model):
    link_title = models.CharField(max_length=500, null=True)
    link_author = models.CharField(max_length=500, null=True)
    user_link = models.CharField(max_length=1000)
    def __str__(self):
        return self.link_title

# Including documents
class AutomatedDocument(models.Model):
    document_title = models.CharField(max_length=500, null=True)
    dcument_author = models.CharField(max_length=500, null=True)
    user_document = models.CharField(max_length=1000)
    def __str__(self):
        return self.document_title

class ReleaseDocument(models.Model):
    document_title = models.CharField(max_length=500, null=True)
    document_author = models.CharField(max_length=500, null=True)
    user_document = models.CharField(max_length=1000)
    def __str__(self):
        return self.document_title

class BugDocument(models.Model):
    document_title = models.CharField(max_length=500, null=True)
    document_author = models.CharField(max_length=500, null=True)
    user_document = models.CharField(max_length=1000)
    def __str__(self):
        return self.document_title

# Including specific pages
class AutomatedPage(models.Model):
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    precondition = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    parameters = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    image = models.ImageField(upload_to='auto_images/', default='auto_images/', blank=True, null=True)
    link = models.ForeignKey(AutomatedLink, blank=True, null=True)
    document_link = models.FileField(upload_to='auto_documents/', default='auto_documents/', blank=True, null=True)
    def get_document_url(self):
        if self.file:
            document_link = models.FileField(upload_to='auto_documents/', default='auto_documents/', blank=True, null=True)
        return 'auto_documents/' + self.file.name
    def __str__(self):
        return self.title

class ReleasePage(models.Model):
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=1000, null=True)
    precondition = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    parameters = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    image = models.ImageField(upload_to='release_images/', default='release_images/', blank=True, null=True)
    link = models.ForeignKey(ReleaseLink, blank=True, null=True)
    def get_document_url(self):
        if self.file:
            document_link = models.FileField(upload_to='release_documents/', default='release_documents/', blank=True, null=True)
            return 'release_documents/' + self.file.name
    def __str__(self):
        return self.title

class BugPage(models.Model):
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=1000, null=True)
    precondition = models.TextField(blank=True)
    steps = models.TextField(blank=True)
    parameters = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    image = models.ImageField(upload_to='bug_images/', default='bug_images/', blank=True, null=True)
    link = models.ForeignKey(BugLink, blank=True, null=True)
    def get_document_url(self):
        if self.file:
            document_link = models.FileField(upload_to='bug_documents/', default='bug_documents/', blank=True, null=True)
            return 'bug_documents/' + self.file.name
    def __str__(self):
        return self.title

class DisplayFrontImages(models.Model):
    image = models.ImageField(upload_to='web_images/', default='web_images/', blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

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
