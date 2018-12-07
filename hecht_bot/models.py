# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Helper(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=30)


class WorkingEntry(models.Model):
    date = models.DateField(_('Datum'))
    helper = models.ForeignKey(
        Helper,
        verbose_name=_('Helfer'),
        related_name='helper',
        on_delete=models.SET_NULL,
        null=True)
