from django.conf.urls import patterns, include, url
from django.http import HttpResponse

from main.views import home, quest, decision, noway

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),

    url(r'^(\w+)$', quest),
    url(r'^(\w+)/(\w+)$', decision),

    url(r'^.+$', noway),
)
