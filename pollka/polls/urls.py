# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('pollka.polls.views',
    url(r'^create/$', 'create'),
    url(r'^(?P<show_hash>\w+)/$', 'show'),
    url(r'^(?P<show_hash>\w+)/(?P<edit_hash>\w+)/edit/$', 'edit'),
    url(r'^(?P<show_hash>\w+)/(?P<edit_hash>\w+)/delete/$', 'delete'),
)
