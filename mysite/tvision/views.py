# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from tvision.models import AutoPage, ReleasePage, BugPage

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
    #Generating counts of the main objects
    auto_name = AutoPage.objects.all()
    release_name = ReleasePage.objects.all()
    bug_name = BugPage.objects.all()

    context = {
        'auto' : auto_name,
        'release' : release_name,
        'bugs' : bug_name,
    }

    return render(request, "home.html", context)

def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            save_form = AutoPage.objects.get(pk=course_id)
            save_form.model_pic = form.cleaned_data['image']
            save_form.save()
            return HttpResponse('Image Uploaded')
        return HttpResponse('Allowed only via POST')
