# -*- coding: utf-8 -*-

from bootstrap.forms import BootstrapForm, Fieldset
from bootstrap.widgets import EmailInput
from django import forms


class ContactForm(BootstrapForm):
    subject = forms.CharField(label='Subject', max_length=40, error_messages={'required': 'Please provide a subject'},
            widget=forms.TextInput(attrs={'class': 'input-xlarge focused', 'autofocus': ''}))
    message = forms.CharField(label='My message', error_messages={'required': 'Didn\'t you want to send us a message?'},
            widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    sender = forms.EmailField(label='My e-mail address', error_messages={'required': 'Please enter your e-mail address'},
            widget=EmailInput(attrs={'class': 'input-xlarge'}))
    cc_myself = forms.BooleanField(label='CC myself', help_text='Do you want a copy of your message?', required=False)

    class Meta:
        layout = (Fieldset('Send us a message', 'subject', 'message', 'sender', 'cc_myself'),)
