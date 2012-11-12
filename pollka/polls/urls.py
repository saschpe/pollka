# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from forms import poll_wizard_view_factory


urlpatterns = patterns('pollka.polls.views',
    url(r'^wizard/$', poll_wizard_view_factory(), name='poll-wizard'),
    #url(r'^create/$', 'create', name='poll-create'),
    url(r'^(?P<show_hash>\w+)/$', 'show', name='poll-show'),
    url(r'^(?P<show_hash>\w+)/(?P<edit_hash>\w+)/edit/$', 'edit', name='poll-edit'),
    url(r'^(?P<show_hash>\w+)/(?P<edit_hash>\w+)/delete/$', 'delete', name='poll-delete'),
)
