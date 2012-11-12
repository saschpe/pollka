# -*- coding: utf-8 -*-

from bootstrap.forms import BootstrapForm, BootstrapModelForm, Fieldset
from bootstrap.widgets import EmailInput
from django import forms
from django.contrib.formtools.wizard.views import SessionWizardView
from models import Choice, Poll


class PollFormMetaMixin:
    '''Meta configuration for all Poll forms.
    '''
    model = Poll
    widgets = {
            'title': forms.TextInput(attrs={'class': 'input-xlarge', 'autofocus': ''}),
            'description': forms.Textarea(attrs={'class': 'input-xlarge', 'rows': 6}),
            'author_name': forms.TextInput(attrs={'class': 'input-xlarge'}),
            'author_email': EmailInput(attrs={'class': 'input-xlarge'}),}


class PollForm1(BootstrapModelForm):
    class Meta(PollFormMetaMixin):
        layout = (Fieldset('Create new poll', 'title', 'description', 'author_name', 'author_email'),)


class PollForm2(BootstrapModelForm):
    class Meta(PollFormMetaMixin):
        layout = (Fieldset('Add some advanced settings', 'hidden', 'voter_limit'),)


class PollForm(BootstrapModelForm):
    class Meta(PollFormMetaMixin):
        layout = (
                Fieldset('Basics', 'title', 'description'),
                Fieldset('Advanced', 'hidden', 'voter_limit'),)


class ChoiceForm(BootstrapModelForm):
    class Meta:
        model = Choice


class ChoiceFormSet(forms.formsets.BaseFormSet):
    pass


class PollWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)
        import pdb;pdb.set_trace()
        poll = Poll.objects.create(
                title = data['title'],
                description = data['description'],
                author = request.user, # Is None for anonymous users
                author_name = data.get('author_name', ''), # Missing in form for authenticated users
                author_email = data.get('author_email', ''), # Missing in form for authenticated users
                hidden = data.get('hidden', False),
                voter_limit = data.get('voter_limit', None))
        return redirect('poll-edit', show_url=poll.show_url, edit_hash=poll.edit_hash)


def poll_wizard_view_factory():
    return PollWizard.as_view([PollForm1, PollForm2])
