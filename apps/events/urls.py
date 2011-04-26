from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required

from surlex.dj import surl

from views import EventListView, EventDetailView

urlpatterns = patterns('',
    url(r'^$', login_required(EventListView.as_view()), name='event_list'),
    surl(r'^event/<pk:s>/$', login_required(EventDetailView.as_view()), name='event_detail'),
)

