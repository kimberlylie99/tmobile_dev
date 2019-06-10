# -*- coding: utf-8 -*-
#import datetime
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

import csv
from django.http import HttpResponse

# Create your models here.
class AutoPage(models.Model):
    pub_date = models.DateTimeField('date published')
    title_text = models.CharField(max_length=1000)
    description_text = models.TextField(blank=True)
    def __str__(self):
        return self.title_text

class ReleasePage(models.Model):
    pub_date = models.DateTimeField('date published')
    title_text = models.CharField(max_length=200)
    description_text = models.TextField(blank=True)
    def __str__(self):
        return self.title_text

class BugPage(models.Model):
    pub_date = models.DateTimeField('date published')
    title_text = models.CharField(max_length=200)
    description_text = models.TextField(blank=True)
    def __str__(self):
        return self.title_text

# trying to export data
def user_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="filename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row','Foo','Bar'])

    return response
