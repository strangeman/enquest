# -*- coding: UTF-8 -*-

from django import forms

from main.models import Team, Quest

class TeamForm(forms.Form):
	team = forms.ModelChoiceField(Team.objects.all())

class QuestForm(forms.Form):
	quest = forms.ModelChoiceField(Quest.objects.all())