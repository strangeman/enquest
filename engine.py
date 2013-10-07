# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.template import RequestContext
from django.forms.util import ErrorList
from django.core.exceptions import ObjectDoesNotExist

from main.models import Token, Quest, Decision
from main.settings import SITE_ROOT

def write_current_decision(dec_obj,token_obj):
    token_obj.decision = dec_obj
    token_obj.save()

def noway(is_ajax=False):
    # if is_ajax:
    #     return render_to_response('noway_ajax.tmpl')
    # else:
    #     return render_to_response('noway.tmpl')
    return render_to_response('noway.tmpl', {'is_ajax': is_ajax, 'site_root': SITE_ROOT})

def get_quest_response(token, template, is_ajax=False):
    try:
        token_obj = Token.objects.get(tok_hash=token)
    except ObjectDoesNotExist:
        return noway(is_ajax)

    if is_ajax:
        if token_obj.decision != None and not token_obj.demo:
            return redirect(SITE_ROOT+'/d/'+str(token)+'/'+str(token_obj.decision.dec_hash))
   
    quest = token_obj.linked_quest
    decision_list = Decision.objects.filter(Q(quest=quest))
    decision_to_tmpl = []
    for decision in decision_list:
        check = False
        if decision == token_obj.decision:
            check = True
        decision_to_tmpl.append({'text': decision.text, 'dec_hash': decision.dec_hash, 'check': check})
    return render_to_response(template, {'quest': quest, 'decisions': decision_to_tmpl, 'token': token_obj.tok_hash, 'is_ajax': is_ajax, 'site_root': SITE_ROOT})

def get_decision_response(token, dec_hash, template, is_ajax=False):
    try:
        dec_obj = Decision.objects.get(dec_hash=dec_hash)
    except ObjectDoesNotExist:
        return noway(is_ajax)
    try:
        token_obj = Token.objects.get(tok_hash=token)
    except ObjectDoesNotExist:
        return noway(is_ajax)   

    if not token_obj.visible:
        return noway(is_ajax)

    if token_obj.demo:
        if token_obj.decision != dec_obj:
            write_current_decision(dec_obj,token_obj)
        return render_to_response(template, {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type, 'is_ajax': is_ajax, 'site_root': SITE_ROOT})

    if token_obj.decision == None:
        write_current_decision(dec_obj,token_obj)
        return render_to_response(template, {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type, 'is_ajax': is_ajax, 'site_root': SITE_ROOT})
    elif token_obj.decision == dec_obj:
        return render_to_response(template, {'decision': dec_obj, 'token':token_obj.tok_hash, 'reward_type':dec_obj.reward_type, 'is_ajax': is_ajax, 'site_root': SITE_ROOT})
    else:
        return noway(is_ajax)

