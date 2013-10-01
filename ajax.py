# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.template import RequestContext
from django.forms.util import ErrorList
from django.utils import simplejson

from main.models import Token, Quest, Decision

def quest_ajax(request, token):
    try:
        token_obj = Token.objects.get(tok_hash=token)
    except ObjectDoesNotExist:
        return render_to_response('noway.tmpl')
    quest = Token.objects.get(tok_hash=token).linked_quest
    decision_list = Decision.objects.filter(Q(quest=quest))
    decision_to_tmpl = []
    for decision in decision_list:
        check = False
        if decision == token_obj.decision:
            check = True
        decision_to_tmpl.append({'text': decision.text, 'dec_hash': decision.dec_hash, 'check': check})
    return render_to_response('quest_ajax.tmpl', {'quest': quest, 'decisions': decision_to_tmpl, 'token': token})

def quest_ajax_test(request):
    return render_to_response('test_quest_ajax.tmpl')
