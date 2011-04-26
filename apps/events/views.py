# Create your views here.

from django.views.generic import ListView, DetailView
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.conf import settings

from models import Event


class EventListView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        context['can_view_report'] = self.request.user.has_perm('events.can_view_report')
        return context


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


class ReportListView(ListView):
    model = Event
    template_name = 'events/report_list.html'

    def dispatch(self, request, *args, **kwargs):
        @permission_required('events.can_view_report')
        def wrapper(request, *args, **kwargs):
            return super(ReportListView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


class ReportDetailView(DetailView):
    model = Event
    template_name = 'events/report_detail.html'

    def dispatch(self, request, *args, **kwargs):
        @permission_required('events.can_view_report')
        def wrapper(request, *args, **kwargs):
            return super(ReportDetailView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


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


