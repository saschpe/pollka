# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from pollka.util import generate_short_hash


class Poll(models.Model):
    title = models.CharField(max_length=256, help_text='Provide an expressive title for your poll.')
    description = models.TextField(blank=True, help_text='Describe your poll.')
    author = models.ForeignKey(User, blank=True, null=True)
    author_name = models.CharField('your name', max_length=64, blank=True)
    author_email = models.EmailField('your e-mail address', blank=True, help_text='If you supply an e-mail address, you will receive the link to administer your poll')
    hidden = models.BooleanField(help_text='Only you can see the answers.')
    voter_limit = models.IntegerField(blank=True, help_text='As soon as the indicated limit has been reached, the poll will be closed.', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    show_hash = models.CharField(editable=False, max_length=12, default=generate_short_hash)
    edit_hash = models.CharField(editable=False, max_length=12, default=generate_short_hash)

    def __unicode__(self):
        return self.title

    def clean(self):
        if self.author is not None and (self.author_name is not None or self.author_email is not None):
            raise ValidationError('Provide either \'author\' for authenticated users or \'author_name\' (optionally with \'author_email\') for anonymous users.')

    @models.permalink
    def get_absolute_url(self):
        return ('pollka.polls.views.show', (), {'show_hash': self.show_hash})


class Choice(models.Model):
    '''Stores a choice for :model:`Poll`.
    '''
    choice = models.CharField(max_length=256)
    poll = models.ForeignKey(Poll)
    vote_limit = models.IntegerField(blank=True, null=True)
    voter_set = models.ManyToManyField(User)

    def __unicode__(self):
        return self.choice
