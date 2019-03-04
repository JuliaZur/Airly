from django.shortcuts import render
from mysite.longLatParser import *
from mysite.cityParser import *
from mysite.idParser import *
from mysite.map import *

def home(request):
    if(request.GET.get('Search')):
        req = request.GET.get('clientRequest')
        if "," in req:
            values = req.split(',')
            result = GeoParser(values[0],values[1])
        elif req.isdigit():
            result = SensorParser(req)
        else: result = CityParser(req)
        return render(request, 'result.html', {'Measurements': result})
    if(request.GET.get('Map')):
        result = Map()
        return render(request,'map.html',{'Measurements': result})

    return render(request, 'home.html')