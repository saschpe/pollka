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
            (None,       {'fields': ('poll', 'choice')}),
            ('Settings', {'fields': ('vote_limit',), 'classes': ('collapse closed',)}))
    inlines = (VotersInline,)


class ChoiceInline(admin.StackedInline):
    model = Choice
    fieldsets = ChoiceAdmin.fieldsets
    extra = 1


class PollAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'description', 'author', 'author_name', 'author_email',
                    'hidden', 'voter_limit', 'created', 'updated', 'show_hash', 'edit_hash')
    search_fields = ('title', 'author__username', 'author_name', 'author_email', 'show_hash', 'edit_hash')
    fieldsets = (
            (None,       {'fields': ('title', 'description')}),
            ('Author',   {'fields': ('author', 'author_name', 'author_email')}),
            ('Settings', {'fields': ('hidden', 'voter_limit'), 'classes': ('collapse closed',)}))
    inlines = (ChoiceInline,)


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Poll, PollAdmin)
