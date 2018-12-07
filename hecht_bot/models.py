# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Helper(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=30)

    def __str__(self):
        return self.name


class HelpingEntry(models.Model):
    date = models.DateField(_('Datum'))
    helper = models.ManyToManyField(
        Helper,
        verbose_name=_('Helfer'),
        related_name='helping_entries')

    @property
    def datum(self):
        return self.date.strftime('%A, %d. %b, %Y')

    def __str__(self):
        return self.date_verbose
