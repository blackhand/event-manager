from django.conf.urls.defaults import patterns, include, url

from surlex.dj import surl

from views import EventListView, EventDetailView

urlpatterns = patterns('',
    url(r'^$', EventListView.as_view(), name='event_list'),
    surl(r'^$', EventDetailView.as_view(), name='event_detail'),
)

