# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from pollka.util import generate_short_hash


class Poll(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User)
    hidden = models.BooleanField(help_text='Only you can see the answers.')
    voter_limit = models.IntegerField(blank=True, help_text='As soon as the indicated limit has been reached, the poll will be closed.', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    show_hash = models.CharField(editable=False, max_length=12, default=generate_short_hash)
    edit_hash = models.CharField(editable=False, max_length=12, default=generate_short_hash)

    @models.permalink
    def get_absolute_url(self):
        return ('polls.views.show', (), {'show_hash': self.show_hash})

    def __unicode__(self):
        return self.title


class Choice(models.Model):
    '''Stores a choice for :model:`Poll`.
    '''
    choice = models.CharField(max_length=256)
    poll = models.ForeignKey(Poll)
    vote_limit = models.IntegerField(blank=True, null=True)
    voter_set = models.ManyToManyField(User)

    def __unicode__(self):
        return self.choice
