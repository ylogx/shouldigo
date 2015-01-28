from django.shortcuts import render
from django.http import HttpResponse

import urllib
import json
from weathercheck.checker import Checker

# Create your views here.
def index(request):
    return HttpResponse('Hi welcome to the homepage')   #TODO

def today(request):
    ''' Main view for today's weather
    '''
    checker = Checker()
    ip = checker.get_ip(request)
    location = checker.get_location(ip)
    weather = checker.weather_check(location)
    context = {'ip': ip, 'location': location, 'weather': weather}
    return render(request, 'weathercheck/today.html', context)
