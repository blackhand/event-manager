# -*- coding: utf-8 -*-

from django import forms
from django.db import models
from django.conf import settings

try:
    from south.modelsinspector import add_introspection_rules
    south_support = True
except ImportError:
    south_support = False


class LocationPickerWidget(forms.TextInput):
    """ Custom Widget for Google Maps coordinates """
    class Media:
        css = {
            'all': (
                settings.STATIC_URL + 'css/location_picker.css',
            )
        }
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
            'http://www.google.com/jsapi?key=' + settings.GMAPS_API_KEY,
            settings.STATIC_URL + 'js/jquery.location_picker.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(LocationPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if None == attrs:
            attrs = {}
        attrs['class'] = 'location_picker'
        return super(LocationPickerWidget, self).render(name, value, attrs)


class LocationField(models.CharField):
    """ Redefined Field for storage google maps coordinates """
    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidget
        return super(LocationField, self).formfield(**kwargs)


if south_support:
    add_introspection_rules([], ["^buildings\.fields\.LocationField"])

