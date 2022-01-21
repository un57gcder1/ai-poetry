from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpRequest
import subprocess
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"
    temperature = None
    length = None

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['temperature'] = self.request.GET.get('temperature')
        context['length'] = self.request.GET.get('length')
        length = self.request.GET.get('length')
        temperature = self.request.GET.get('temperature')
        context['result'] = subprocess.check_output(['th', 'sample.lua', '-gpu', '-1', '-checkpoint', 'cv/checkpoint_251450.t7', '-temperature ', str(temperature), '-length ', str(length)]).stdout.decode('utf-8')
        return context

        

        
        
