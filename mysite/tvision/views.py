# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from tvision.models import AutomatedPage, ReleasePage, BugPage, StartDateForm, EndDateForm
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView

# for pie chart stuff
from matplotlib import pylab
from matplotlib import pyplot as plt
from pylab import *
import PIL, PIL.Image, StringIO

import matplotlib
matplotlib.axes.Axes.pie
matplotlib.pyplot.pie

# displaying home page
def home(request):
        startDate = request.GET.get('start_date')
        endDate = request.GET.get('end_date')

        if startDate and endDate:
            auto_data = AutomatedPage.objects.filter(pub_date__range=[startDate,endDate])
            release_data = ReleasePage.objects.filter(pub_date__range=[startDate,endDate])
            bug_data = BugPage.objects.filter(pub_date__range=[startDate,endDate])
        else:
            automated_data = AutomatedPage.objects.all()
            release_data = ReleasePage.objects.all()
            bug_data = BugPage.objects.all()

        context = {
            'auto' : automated_data,
            'release' : release_data,
            'bugs' : bug_data,
            'start_date' : StartDateForm,
            'end_date' : EndDateForm,
        }

        return render(request, "home.html", context)

# allowing user to upload image
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

#    labels = 'Frogs','Hogs','Dogs','Logs'
#    sizes = [15,30,45,10]
#    explode = (0,0.05,0,0)

#    fig1,ax1 = plt.subplots()
#    ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90,output_type='div')

#    ax1.axis('equal')
#    title('Raining Hogs and Dogs',bbox={'facecolor':'0.8','pad':5})

#    plt.show()

#   constructing the graph
    x = arrange(0, 2*pi, 0.01)
    s = cos(x)**2
    plot(x,s)

    xlabel('xlabel(x)')
    ylabel('ylabel(y)')
    title('simple graph')
    grid(True)

#   store image in a string buffer
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostrong_rgb())
    pilImage.save(buffer, "PNG")
    pilImage.save('media/web_images/chart.png')
    pylab.close()

#   try 2
    labels = 'Frogs','Hogs','Dogs','Logs'

    sizes = [15,30,45,10]

#    colors = ['r', 'y', 'g', 'b']

    explode = (0,0.1,0,0)

    fig1,ax1 = plt.subplots()

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

    ax1.axis('equal')

#    plt.legend()

    fig1.show()
    fig1.savefig("media/web_images/chart.png")

#   send buffer to browser
    return HttpResponse(buffer.getvalue(), content_type="image/png")
    return render(request)
