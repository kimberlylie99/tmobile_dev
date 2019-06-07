# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from tvision.models import Auto, ReleasePage, BugPage

from django.views.generic import TemplateView

# Create your views here.

def home(request):
    """View function for home page of site"""

    #Generating counts of the main objects
    num_auto = Auto.objects.all().count()
    num_release = ReleasePage.objects.all().count()
    num_bug = BugPage.objects.all().count()

    context = {
        'auto' : num_auto,
        'release' : num_release,
        'bugs' : num_bug,
    }
    return render(request, '/mysite/static/home.html')

class HomeView(TemplateView):
    template_name = 'home.html'
