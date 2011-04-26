# Create your views here.

from django.views.generic import ListView, DetailView
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
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

        event = self.object
        user = self.request.user

        context['user_suscribed'] = event.suscribed(user)

        return context



def event_register(request, pk):
    """
    register event view, quickly register and redirect to the detail view again
    """
    event = get_object_or_404(Event, id=pk)
    if not event.suscribed(request.user):
        event.suscribed_users.add(request.user)
        event.vacants -= 1
        event.save()

    return HttpResponseRedirect(reverse('event_detail', args=[pk]))
