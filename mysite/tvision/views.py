# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from tvision.models import AutomatedPage, ReleasePage, BugPage, StartDateForm, EndDateForm
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView

from django.core.files.storage import FileSystemStorage

# displaying home page
def home(request):
        startDate = request.GET.get('start_date')
        endDate = request.GET.get('end_date')

        if startDate and endDate:
            automated_data = AutomatedPage.objects.filter(pub_date__range=[startDate,endDate])
            release_data = ReleasePage.objects.filter(pub_date__range=[startDate,endDate])
            bug_data = BugPage.objects.filter(pub_date__range=[startDate,endDate])
        else:
            automated_data = AutomatedPage.objects.all()
            release_data = ReleasePage.objects.all()
            bug_data = BugPage.objects.all()

        context = {
            'auto' : automated_data,
            'release' : release_data,
            'bug' : bug_data,
            'start_date' : StartDateForm,
            'end_date' : EndDateForm
        }

        return render(request, "home.html", context)

# allowing user to upload image
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage(location='/media/documents')
        fs.save(uploaded_file.name, uploaded_file)
