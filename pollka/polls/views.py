# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect, render
from models import Choice, Poll
#from forms import PollForm


#def create(request):
#   if request.method == 'POST': # If the form has been submitted...
#       form = PollForm(request.POST) # A form bound to the POST data
#       if form.is_valid(): # All validation rules pass
#           poll = Poll.objects.create(
#                   title = form.cleaned_data['title'],
#                   description = form.cleaned_data['description'],
#                   author = request.user, # Is None for anonymous users
#                   author_name = form.cleaned_data.get('author_name', ''), # Missing in form for authenticated users
#                   author_email = form.cleaned_data.get('author_email', ''), # Missing in form for authenticated users
#                   hidden = form.cleaned_data('hidden', False), # Optional
#                   voter_limit = form.cleaned_data('voter_limit', None)) # Optional
#           return redirect(poll)
#   else:
#       form = PollForm() # An unbound form
#   return render(request, 'polls/create.html', {'form': form})


#def choices(request, show_hash):
#   if request.method == 'POST': # If the form has been submitted...
#       pass
#   else:
#       form = ChoiceForm() # An unbound form
#   return render(request, 'polls/choices.html', {'form': form})


def show(request, show_hash):
    try:
        poll = Poll.objects.get(show_hash=show_hash)
    except Poll.DoesNotExist:
        return redirect('poll-create')
    return render(request, 'polls/show.html', {'poll': poll})


def edit(request, show_hash, edit_hash):
    try:
        poll = Poll.objects.get(show_hash=show_hash, edit_hash=edit_hash)
    except Poll.DoesNotExist:
        return redirect('poll-create')
    return render(request, 'polls/edit.html', {'poll': poll})


def delete(request, show_hash, edit_hash):
    pass
   #try:
   #    poll = Poll.objects.get(show_hash=show_hash, edit_hash=edit_hash)
   #except Poll.DoesNotExist:
   #    return redirect('poll-create')
   #return render(request, 'polls/delete.html', {'poll': poll})
