# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
import requests
import json


def suggest(request, word):
    r = requests.get('http://localhost:8983/solr/somali/select?q=en:' + word + '*');
    response = r.json();
    suggestions = [];
    for doc in response['response']['docs']:
        suggestions.append(doc['en'][0]);
    return HttpResponse(json.dumps({'suggestions': suggestions}, indent=4))

def translation(request, word):
    template = loader.get_template('translation.html')
    r = requests.get('http://localhost:8983/solr/somali/select?q=en:"' + word + '"');
    response = r.json();
    context = {"words":response['response']['docs']}
    return HttpResponse(template.render(context, request))