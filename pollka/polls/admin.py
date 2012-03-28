# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Choice, Poll


class VotersInline(admin.StackedInline):
    model = Choice.voter_set.through


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice', 'poll', 'vote_limit')
    list_filter = ('poll__show_hash', 'vote_limit')
    search_fields = ('choice', 'poll__show_hash', 'vote_limit')
    fieldsets = (
        (None,          {'fields': ('poll', 'choice')}),
        ('Settings',    {'fields': ('vote_limit',), 'classes': ('collapse closed',)}),
    )
    inlines = (VotersInline,)


class ChoiceInline(admin.StackedInline):
    model = Choice
    fieldsets = ChoiceAdmin.fieldsets
    extra = 1


class PollAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'description', 'author', 'hidden', 'voter_limit', 'created', 'updated', 'show_hash', 'edit_hash')
    list_filter = ('author__username', 'hidden')
    search_fields = ('title', 'author__username', 'show_hash', 'edit_hash')
    fieldsets = (
        (None,                  {'fields': ('title', 'description', 'author')}),
        ('Settings',            {'fields': ('hidden', 'voter_limit'), 'classes': ('collapse closed',)}),
        #('Date information',    {'fields': ('created', 'updated'), 'classes': ('collapse closed',)}),
        #('Hashes',              {'fields': ('show_hash', 'edit_hash'), 'classes': ('collapse closed',)}),
    )
    inlines = (ChoiceInline,)


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Poll, PollAdmin)
