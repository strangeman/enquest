# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response

from main.models import Token, Quest, Decision
from main.engine import get_quest_response, get_decision_response, noway
from django.http import HttpResponse

def home(request):
    return render_to_response('home.tmpl')

def quest(request, token):
    return get_quest_response(token, 'quest.tmpl', False)

def decision(request, token, dec_hash):
    return get_decision_response(token, dec_hash, 'decision.tmpl', False)

def quest_ajax(request, token):
    return get_quest_response(token, 'quest.tmpl', True)

def decision_ajax(request, token, dec_hash):
    return get_decision_response(token, dec_hash, 'decision.tmpl', True)

def quest_ajax_test(request):
    return render_to_response('test_quest_ajax.tmpl')

def badpage(request):
    return noway(False)