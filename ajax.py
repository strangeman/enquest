# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.template import RequestContext
from django.forms.util import ErrorList
from django.shortcuts import redirect

from main.models import Token, Quest, Decision

def quest_ajax(request, token):
    try:
        token_obj = Token.objects.get(tok_hash=token)
    except ObjectDoesNotExist:
        return render_to_response('noway.tmpl')

    if token_obj.decision != None and not token_obj.demo:
        return redirect('/d/'+str(token)+'/'+str(token_obj.decision.dec_hash))

    quest = Token.objects.get(tok_hash=token).linked_quest
    decision_list = Decision.objects.filter(Q(quest=quest))
    decision_to_tmpl = []
    for decision in decision_list:
        check = False
        if decision == token_obj.decision:
            check = True
        decision_to_tmpl.append({'text': decision.text, 'dec_hash': decision.dec_hash, 'check': check})
    return render_to_response('quest_ajax.tmpl', {'quest': quest, 'decisions': decision_to_tmpl, 'token': token})

def write_current_decision(dec_obj,token_obj):
    token_obj.decision = dec_obj
    token_obj.save()

def decision_ajax(request, token, dec_hash):
    try:
        dec_obj = Decision.objects.get(dec_hash=dec_hash)
    except ObjectDoesNotExist:
        return render_to_response('noway.tmpl')
    try:
        token_obj = Token.objects.get(tok_hash=token)
    except ObjectDoesNotExist:
        return render_to_response('noway.tmpl')   

    if not token_obj.visible:
        return render_to_response('noway.tmpl')

    if token_obj.demo:
        if token_obj.decision != dec_obj:
            write_current_decision(dec_obj,token_obj)
        return render_to_response('decision_ajax.tmpl', {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type})

    if token_obj.decision == None:
        write_current_decision(dec_obj,token_obj)
        return render_to_response('decision_ajax.tmpl', {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type})
    elif token_obj.decision == dec_obj:
        return render_to_response('decision_ajax.tmpl', {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type})
    else:
        return render_to_response('noway.tmpl')

def quest_ajax_test(request):
    return render_to_response('test_quest_ajax.tmpl')
