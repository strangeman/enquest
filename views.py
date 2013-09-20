# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.template import RequestContext
from django.forms.util import ErrorList

from django.core.exceptions import ObjectDoesNotExist

from main.models import Token, Quest, Decision

def home(request):
    return render_to_response('home.tmpl')

def quest(request, token):
    try:
        token_obj = Token.objects.get(tok_hash=token)
    except ObjectDoesNotExist:
        return noway(request)
    quest = Token.objects.get(tok_hash=token).linked_quest
    decision_list = Decision.objects.filter(Q(quest=quest))
    decision_to_tmpl = []
    for decision in decision_list:
        check = False
        if decision == token_obj.decision:
            check = True
        decision_to_tmpl.append({'text': decision.text, 'dec_hash': decision.dec_hash, 'check': check})
    return render_to_response('quest.tmpl', {'quest': quest, 'decisions': decision_to_tmpl, 'token': token})

def write_current_decision(dec_obj,token_obj):
    token_obj.decision = dec_obj
    token_obj.save()

def decision(request, token, dec_hash):
    try:
        dec_obj = Decision.objects.get(dec_hash=dec_hash)
    except ObjectDoesNotExist:
        return noway(request)
    try:
        token_obj = Token.objects.get(tok_hash=token)
    except ObjectDoesNotExist:
        return noway(request)   

    if not token_obj.visible:
        return noway(request)

    if token_obj.demo:
        if token_obj.decision != dec_obj:
            write_current_decision(dec_obj,token_obj)
        return render_to_response('decision.tmpl', {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type})

    if token_obj.decision == None:
        write_current_decision(dec_obj,token_obj)
        return render_to_response('decision.tmpl', {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type})
    elif token_obj.decision == dec_obj:
        return render_to_response('decision.tmpl', {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type})
    else:
        return noway(request)

def noway(request):
    return render_to_response('noway.tmpl')