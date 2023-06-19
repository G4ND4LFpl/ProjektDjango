from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from ProjektDjango.settings import BASE_DIR

import json

# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    context = {}

    if request.method=='GET':
        if request.GET.get('selector'):
            lang = request.GET['selector']
            context = open_json(lang+".json")
        else:
            context = open_json("pl.json")

    return render(request,'index.html',context)

def open_json(filename):
    filename = BASE_DIR + "/warhammer/langs/" + filename
    f = open(filename, encoding="UTF-8")
    data = json.load(f)
    f.close()
    return data