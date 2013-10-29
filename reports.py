# -*- coding: UTF-8 -*-

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from main.models import Token, Quest, Decision, Team
from main.forms import TeamForm, QuestForm
from main.engine import noway

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def scenario(request):
    quest_query = Quest.objects.all()
    dec_query = Decision.objects.all()
    template_tree = []
    for quest in quest_query:
        template_tree.append({'quest': quest, 'dec_list': dec_query.filter(quest=quest)})
    return render_to_response('scenario.tmpl', {'tree': template_tree})

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def gameplay_form(request):
    if request.method == 'POST': 
        form = TeamForm(request.POST)
        if form.is_valid():
            teamid = form.cleaned_data['team'].teamid
            return HttpResponseRedirect(request.path+'/'+str(teamid)) # Redirect after POST 
    else:
        form = TeamForm()
    return render(request, 'team_form.tmpl', {'form': form, 'path': request.path})

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def gameplay(request, team):
    try:
        team_obj = Team.objects.get(teamid=team)
    except ObjectDoesNotExist:
        return noway(False)
    token_list = Token.objects.filter(team=team_obj)
    return render_to_response('gameplay.tmpl', {'tokens': token_list, 'team': team_obj.name, 'host': request.get_host()})


@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def links_form(request):
    if request.method == 'POST': 
        form = QuestForm(request.POST)
        if form.is_valid():
            questid = form.cleaned_data['quest'].id
            return HttpResponseRedirect(request.path+'/'+str(questid)) # Redirect after POST 
    else:
        form = QuestForm()
    return render(request, 'team_form.tmpl', {'form': form, 'path': request.path})

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def links(request, quest):
    try:
        quest_obj = Quest.objects.get(id=quest)
    except ObjectDoesNotExist:
        return noway(False)
    token_list = Token.objects.filter(linked_quest=quest_obj)
    return render_to_response('links.tmpl', {'quest': quest_obj, 'tokens': token_list, 'host': request.get_host()})