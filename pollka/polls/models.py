# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #max_participants = models.IntegerField(blank=True)
    #vote_limit = models.IntegerField(blank=True)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=256)


class Vote(models.Model):
    choice = models.ForeignKey(Choice)
    user = models.ForeignKey(User)


# We may want to override User model and add country, timezone, gender, age, etc
