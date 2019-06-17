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
        startDate = request.GET.get('startDate')
        endDate = request.GET.get('endDate')

        parsed_start_date = None
        parsed_end_date = None

        if startDate and endDate:
            errors = {}
            try:
                parsed_start_date = datetime.datetime.strptime(startDate, "%d/%m/%Y")
            except ValueError as e:
                errors["startDate"] = "Invalid date"
            try:
                parsed_end_date = datetime.datetime.strptime(endDate, "%d/%m/%Y")
            except ValueError as e:
                errors["endDate"] = "Invalid date"

        if startDate and endDate:
            data = AutoPage.objects.filter(date_range=[parsed_start_date,parsed_end_date])
        else:
            data = AutoPage.objects.none()

        #Generating counts of the main objects
        #auto_name = AutoPage.objects.all().filter(startDate__gte=startDate, endDate__lte=endDate)
        #release_name = ReleasePage.objects.all().filter(startDate__gte=startDate, endDate__lte=endDate)
        #bug_name = BugPage.objects.all().filter(startDate__gte=startDate, endDate__lte=endDate)

        auto_name = AutoPage.objects.all()
        release_name = ReleasePage.objects.all()
        bug_name = BugPage.objects.all()

        context = {
            #'auto' : auto_name,
            'release' : release_name,
            'bugs' : bug_name,
            'start_date' : startDate,
            'end_date' : endDate,
            'data' : data,
        }

        return render(request, "home.html", context)

def upload_pic(request):
    album = get_object_or_404(AutoPage, pk=1)
    return render(request, 'home.html', {'auto_pic':auto_pic})
