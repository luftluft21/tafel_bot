# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Helper
from .models import HelpingEntry


class HelpingEntryAdmin(admin.ModelAdmin):
    list_display = ('datum',)
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('date',)


admin.site.register(Helper)
admin.site.register(HelpingEntry, HelpingEntryAdmin)
