# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from tvision.models import AutoPage, ReleasePage, BugPage, StartDateForm, EndDateForm
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView

# for pie chart stuff
from pylab import *

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

# adding pie chart
# https://github.com/agiliq/django-graphos
# https://github.com/sainipray/neerajbyte
#def piechart(request):
#    """piechart stuff"""
#    xdata = ["passed","blocked","retest","rollback-passed","rollback-failed","conditional","failed"]
#    ydata = [75,0,0,0,0,10,15]

def piechart(request):
#    figure(1,figsize(6,6))
#    ax = axes([0.1,0.1,0.8,0.8])

    labels = 'Frogs','Hogs','Dogs','Logs'
    sizes = [15,30,45,10]
    explode = (0,0.05,0,0)

    fig1,ax1 = plt.subplots()
    ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90,output_type='div')

    ax1.axis('equal')
#    title('Raining Hogs and Dogs',bbox={'facecolor':'0.8','pad':5})

    plt.show()
