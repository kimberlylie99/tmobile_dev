from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url('', TemplateView.as_view(template_name='home.html')),
]
    #url('', views.home, name='home'),
    #url('', TemplateView.as_view(template_name='home.html')),
