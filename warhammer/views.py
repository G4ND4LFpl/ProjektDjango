from django.shortcuts import render
from django.http import HttpRequest
from ProjektDjango.settings import BASE_DIR

import json

# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    print('debug: test 1/3')
    context = {}

    if request.method=='GET':
        print('debug: test 2/3')

        if request.GET.get('selector'):
            lang = request.GET['selector']
            context = open_json(lang+".json")
        else:
            context = open_json("en.json")

    return render(request,'index.html',context)

def open_json(filename):
    filename = BASE_DIR + "\\warhammer\\langs\\" + filename
    f = open(filename)
    data = json.load(f)
    f.close()
    return data