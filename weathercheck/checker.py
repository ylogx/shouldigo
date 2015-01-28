import urllib
import json

class Checker:
    def _request_json(self, url):
        ''' Send a urllib request for json item
        '''
        req = urllib.request.Request(url)
        json_bytes = urllib.request.urlopen(req).read()
        json_str = json_bytes.decode()
        json_dict = json.loads(json_str)
        return json_dict

    def weather_check(self, location):
        api_key = 'af28f357f23b0ae779a75617eec26398'
        #TODO: Use country in location below
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location
        json_dict = self._request_json(url)
        output = json_dict['weather']
        output = output[0]['main']
        return output

    def get_location(self, ip):
        ''' Get the current location of user via ip-api
        '''
        if ip == '127.0.0.1':
            return 'Delhi'  #FIXME: Use some other location
        url = 'http://ip-api.com/json/' + ip
        json_dict = self._request_json(url)
        city = ''   #FIXME: Fatal, need backup method
        if 'city' in json_dict.keys():
            city = json_dict['city']
        return city

    def get_ip(self, request):
        ''' Get the IP address of user
        '''
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
