# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from tvision.models import Auto, ReleasePage, BugPage

# Create your views here.

def index(request):
    """View function for home page of site"""

    #Generating counts of the main objects
    num_auto = Auto.objects.all().count()
    num_release = ReleasePage.objects.all().count()
    num_bug = BugPage.objects.all().count()

    context = {
        'num_auto' : num_auto,
        'num_release' : num_release,
        'num_bug' : num_bug,
    }

    return render(request, 'views.html', context)
