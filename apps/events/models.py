# -*- coding: utf-8 -*-

from django.db import models
from django.utils.safestring import mark_safe
from datetime import date, datetime

from django.contrib.auth.models import User

from fields import LocationField

# Create your models here.


class EventManager(models.Manager):
    pass


class Event(models.Model):
    """ model representing an Event """
    title = models.CharField('titulo', max_length=64)
    place = LocationField('lugar', max_length=255)
    start_at = models.DateTimeField('fecha y hora')
    vacants = models.PositiveIntegerField('vacantes')
    suscribed_users = models.ManyToManyField(User, verbose_name='usuarios registrados', related_name='events', blank=True, null=True)

    objects = EventManager()
    
    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
    
    def __unicode__(self):
        return u'%s' % self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('event_detail', str(self.pk))

    def map_tag(self):
        coords = self.place
        tag = ('<input type="hidden" name="location" value="%s" class="location_picker read_only" maxlength="255" />') % coords
        return mark_safe(tag)

    def suscribed(self, user):
        return user in self.suscribed_users.all()

