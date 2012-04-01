# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django.shortcuts import render
from pollka.forms import ContactForm


def index(request):
    '''Render a fancy static frontpage.
    '''
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    '''
    '''
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@pollka.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
    return render(request, 'contact.html', {'form': form})


def imprint(request):
    return render(request, 'imprint.html')
