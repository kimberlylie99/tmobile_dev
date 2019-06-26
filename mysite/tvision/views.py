# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from tvision.models import AutoPage, ReleasePage, BugPage, StartDateForm, EndDateForm
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView

def home(request):
        startDate = request.GET.get('start_date')
        endDate = request.GET.get('end_date')

        if startDate and endDate:
            auto_data = AutoPage.objects.filter(pub_date__range=[startDate,endDate])
            release_data = ReleasePage.objects.filter(pub_date__range=[startDate,endDate])
            bug_data = BugPage.objects.filter(pub_date__range=[startDate,endDate])
        else:
            auto_data = AutoPage.objects.all()
            release_data = ReleasePage.objects.all()
            bug_data = BugPage.objects.all()

        context = {
            'auto' : auto_data,
            'release' : release_data,
            'bugs' : bug_data,
            'start_date' : StartDateForm,
            'end_date' : EndDateForm,
        }

        return render(request, "home.html", context)

def upload_pic(request):
    album = get_object_or_404(AutoPage, pk=1)
    return render(request, 'home.html', {'auto_pic':auto_pic})
