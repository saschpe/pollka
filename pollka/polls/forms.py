# -*- coding: utf-8 -*-

from bootstrap.forms import BootstrapForm, BootstrapModelForm, Fieldset
from bootstrap.widgets import EmailInput
from django import forms
from models import Choice, Poll


class PollFormMetaMixin:
    model = Poll
    widgets = {
            'title': forms.TextInput(attrs={'class': 'input-xlarge', 'autofocus': ''}),
            'description': forms.Textarea(attrs={'class': 'input-xlarge', 'rows': 6}),
            'author_name': forms.TextInput(attrs={'class': 'input-xlarge'}),
            'author_email': EmailInput(attrs={'class': 'input-xlarge'}),}


class AnonymousPollForm(BootstrapModelForm):
    class Meta(PollFormMetaMixin):
        layout = (Fieldset('Create new poll', 'title', 'description', 'author_name', 'author_email'),)


class PollForm(BootstrapModelForm):
    class Meta(PollFormMetaMixin):
        layout = (Fieldset('Create new poll', 'title', 'description'),)


class ChoiceForm(BootstrapModelForm):
    class Meta:
        model = Choice
