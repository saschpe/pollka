# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, redirect, render
from models import Choice, Poll
from forms import AnonymousPollForm, PollForm


def create(request):
    if request.method == 'POST': # If the form has been submitted...
        if request.user.is_authenticated():
            form = PollForm(request.POST) # A form bound to the POST data
        else:
            form = AnonymousPollForm(request.POST)
        if form.is_valid(): # All validation rules pass
            poll = Poll.objects.create(
                    title = form.cleaned_data['title'],
                    description = form.cleaned_data['description'],
                    author = request.user, # Is None for anonymous users
                    author_name = form.cleaned_data.get('author_name', ''), # Missing in form for authenticated users
                    author_email = form.cleaned_data.get('author_email', '')) # Missing in form for authenticated users
            #return HttpResponseRedirect('show', poll.show_hash) # Redirect after POST
            return redirect(poll)
    else:
        if request.user.is_authenticated():
            form = PollForm() # An unbound form
        else:
            form = AnonymousPollForm() # An unbound form
    return render(request, 'polls/create.html', {'form': form})


def show(request, show_hash):
   #try:
   #    poll = Poll.objects.get(show_hash=show_hash)
   #except Poll.DoesNotExit:
   #    redirect('create')
    poll = get_object_or_404(Poll, show_hash=show_hash)
    return render(request, 'polls/show.html')


def edit(request, show_hash, edit_hash):
    poll = get_object_or_404(Poll, show_hash=show_hash, edit_hash=edit_hash)
    return render(request, 'polls/edit.html')


def delete(request, show_hash, edit_hash):
    pass
