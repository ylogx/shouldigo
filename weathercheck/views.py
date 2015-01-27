from django.shortcuts import render
from django.http import HttpResponse

import urllib
import json

# Create your views here.
def index(request):
    return HttpResponse('Hi welcome to the homepage')   #TODO

def today(request):
    ''' Main view for today's weather
    '''
    return HttpResponse('Your location is %s and your ip is %s'%(
                            get_location(), get_ip()))


def get_location():
    ''' Get the current location of user via ip-api
    '''
    ip = get_ip()
    url = 'http://ip-api.com/json/' + ip
    req = urllib.request.Request(url)
    json_bytes = urllib.request.urlopen(req).read()
    json_str = json_bytes.decode()
    json_dict = json.loads(json_str)
    city = ''   #FIXME: Fatal, need backup method
    if 'city' in json_dict.keys():
        city = json_dict['city']
    return city

def get_ip():
    ''' Get the IP address of user
    '''
    ip = '14.140.107.130'   #TODO
    return ip
