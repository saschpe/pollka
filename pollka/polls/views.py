# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response
from models import Choice, Poll


def create(request):
    return render_to_response('polls/create.html')


def show(request, show_hash):
   #try:
   #    poll = Poll.objects.get(show_hash=show_hash)
   #except Poll.DoesNotExit:
   #    redirect('create')
    poll = get_object_or_404(Poll, show_hash=show_hash)
    return render_to_response('polls/show.html')


def edit(request, show_hash, edit_hash):
    poll = get_object_or_404(Poll, show_hash=show_hash, edit_hash=edit_hash)
    return render_to_response('polls/edit.html')


def delete(request, show_hash, edit_hash):
    pass
