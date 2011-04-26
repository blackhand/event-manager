# -*- coding: utf-8 -*-

from django.db import models
from datetime import date, datetime
from fields import LocationField

# Create your models here.


class EventManager(models.Manager):
    pass


class Event(models.Model):
    """ model representing an Event """
    title = models.CharField('Titulo', max_length=64)
    place = LocationField('Lugar', max_length=255)
    start_at = models.DateTimeField('Fecha y Hora', blank=True, null=True)
    vacants = models.PositiveIntegerField('Vacantes (0 o dejar en blanco para ilimitado)', blank=True, null=True)

    objects = EventManager()
    
    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
    
    def __unicode__(self):
        return u'%s' % self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('event_detail', str(self.pk))

