# -*- coding: utf-8 -*-

from bootstrap.forms import BootstrapForm, BootstrapModelForm, Fieldset
from bootstrap.widgets import EmailInput
from django import forms
from models import Choice, Poll


class PollForm(BootstrapModelForm):
    class Meta:
        layout = (Fieldset('Create new poll', 'title', 'description', 'author_name', 'author_email'),)
        model = Poll
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-xlarge'}),
            'description': forms.Textarea(attrs={'class': 'input-xlarge'})
            'author_name': forms.TextInput(attrs={'class': 'input-xlarge'})
            'author_email': EmailInput(attrs={'class': 'input-xlarge'})
        }


class ChoiceForm(BootstrapForm):
    class Meta:
        model = Choice
