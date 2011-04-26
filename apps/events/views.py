# Create your views here.

from django.views.generic import ListView, DetailView
from django.utils.safestring import mark_safe
from django.conf import settings

from models import Event


class EventListView(ListView):
    model = Event


class EventDetailView(DetailView):
    model = Event
    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        extra_js = 'http://www.google.com/jsapi?key='+settings.GMAPS_API_KEY
        context['extra_js'] = mark_safe(extra_js)
        return context
