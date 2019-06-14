# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from tvision.models import AutoPage, ReleasePage, BugPage
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    #Generating counts of the main objects
    auto_name = AutoPage.objects.all()
    release_name = ReleasePage.objects.all()
    bug_name = BugPage.objects.all()

    context = {
        'auto' : auto_name,
        'release' : release_name,
        'bugs' : bug_name,
    }

    template_name = 'home.html'

def home(request):
    startDate = request.GET.get('pub_date')
    endDate = request.GET.get('pub_date')

    for pub_date in AutoPage.max_length:
        if pub_date.AutoPage < startDate:
            startDate = pub_date.AutoPage
        elif pub_date.AutoPage > endDate:
            endDate = pub_date.AutoPage

    #Generating counts of the main objects
    auto_name = AutoPage.objects.all().filter(startDate__gte=startDate, endDate__lte=endDate)
    release_name = ReleasePage.objects.all().filter(startDate__gte=startDate, endDate__lte=endDate)
    bug_name = BugPage.objects.all().filter(startDate__gte=startDate, endDate__lte=endDate)

    context = {
        'auto' : auto_name,
        'release' : release_name,
        'bugs' : bug_name,
        'start_date' : startDate,
        'end_date' : endDate,
    }

    return render(request, "home.html", context)

def upload_pic(request):
    album = get_object_or_404(AutoPage, pk=1)
    return render(request, 'home.html', {'auto_pic':auto_pic})
