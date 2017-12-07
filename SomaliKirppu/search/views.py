# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
import requests


def index(request):
    template = loader.get_template('template.html')
    context = {    }
    return HttpResponse(template.render(context, request))
def translation(request, word):
    if word == 'indexhtml':
        template = loader.get_template('index.html')
        context = {    }
        return HttpResponse(template.render(context, request));
    template = loader.get_template('template.html')
    r = requests.get('http://localhost:8983/solr/somali/select?q=en:"' + word + '"');
    response = r.json();

    context = {"word":response['response']['docs'][0]['en'][0],
               "result": response['response']['docs'][0]['so'][0]}
    return HttpResponse(template.render(context, request))

