# -*- coding: utf-8 -*-

from django.contrib import admin

from models import Event


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
