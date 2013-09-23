# -*- coding: UTF-8 -*-

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response

from main.models import Token, Quest, Decision

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def scenario(request):
    quest_query = Quest.objects.all()
    dec_query = Decision.objects.all()
    template_tree = []
    for quest in quest_query:
        template_tree.append({'quest': quest, 'dec_list': dec_query.filter(quest=quest)})
    return render_to_response('scenario.tmpl', {'tree': template_tree})

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def links(request):
    return render_to_response('links.tmpl')

@user_passes_test(lambda u: u.is_staff, login_url='/admin/', redirect_field_name='')
def gameplay(request):
    return render_to_response('gameplay.tmpl')