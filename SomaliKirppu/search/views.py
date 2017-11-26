# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import requests
import json


def index(request):
    template = loader.get_template('index.html')
    context = {    }
    return HttpResponse(template.render(context, request))
def translation(request, word):
    template = loader.get_template('index.html')
    r = requests.get('http://localhost:8983/solr/somali/select?q=en:"' + word + '"');
    response = r.json();

    context = {"word":response['response']['docs'][0]['en'][0],
               "result": response['response']['docs'][0]['so'][0]}
    return HttpResponse(template.render(context, request))

# Create your views here.
