# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.template import RequestContext
from django.forms.util import ErrorList
from django.utils import simplejson

from main.models import Token, Quest, Decision

def quest_ajax(request):
    result = {'quest': 'No quest'}
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'token'):
            token = GET[u'token']
            try:
                token_obj = Token.objects.get(tok_hash=token)
            except ObjectDoesNotExist:
                pass
            quest = Token.objects.get(tok_hash=token).linked_quest
            result = {'quest': quest.text}
    json = simplejson.dumps(result)
    return HttpResponse(json, mimetype='application/json')