# Create your views here.

from django.views.generic import ListView, DetailView

from models import Event

class EventListView(ListView):
    model = Event

class EventDetailView(DetailView):
    model = Event
