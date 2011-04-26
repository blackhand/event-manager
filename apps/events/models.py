# -*- coding: utf-8 -*-

from django.db import models
from datetime import date, datetime

# Create your models here.

class Event(models.Model):
    """ model representing an Event """
    title = models.CharField('Titulo', max_length=64)
    place = models.CharField('Lugar', max_length=255, blank=True)
    start_at = models.DateTimeField('Fecha y Hora', blank=True, null=True)
    
    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
    
    def __unicode__(self):
        return u'%s' % self.title
    
    #@models.permalink
    #def get_absolute_url(self):
    #    return ('event_detail')

