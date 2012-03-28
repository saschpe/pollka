# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pollka.views.index'),
    #url(r'^accounts/', include('pollka.accounts.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^events/', include('pollka.events.urls')),
    url(r'^polls/', include('pollka.polls.urls')),
)
