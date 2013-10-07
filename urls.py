# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.shortcuts import redirect

from main.views import home, quest, decision, quest_ajax, quest_ajax_test, decision_ajax, decision_ajax_taken, badpage
from main.reports import scenario, links, gameplay, links_form, gameplay_form

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', home, name='home'),

    url(r'^q/(\w+)$', quest_ajax),
    url(r'^d/(\w+)/(\w+)$', decision_ajax),
    url(r'^dt/(\w+)/(\w+)$', decision_ajax_taken),
    url(r'^test_q_ajax$', quest_ajax_test),

    url(r'^admin/report/scenario$', scenario),
    url(r'^admin/report/links$', links_form),
    url(r'^admin/report/links/(\w+)$', links),
    url(r'^admin/report/gameplay$', gameplay_form),
    url(r'^admin/report/gameplay/(\w+)$', gameplay),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin$', lambda r: redirect('/admin/')),

    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
    url(r'^(\w+)$', quest),
    url(r'^(\w+)/(\w+)$', decision),


    url(r'^.+$', badpage),
)

