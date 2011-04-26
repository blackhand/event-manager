from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required

from surlex.dj import surl

from views import EventListView, EventDetailView, ReportListView, ReportDetailView

from views import event_register

urlpatterns = patterns('',
    url(r'^$', login_required(EventListView.as_view()), name='event_list'),
    surl(r'^event/<pk:s>/$', login_required(EventDetailView.as_view()), name='event_detail'),
    surl(r'^event/<pk:s>/register', login_required(event_register), name='event_register'),
    surl(r'^report/$', ReportListView.as_view(), name='report_list'),
    surl(r'^report/<pk:s>/$', ReportDetailView.as_view(), name='report_detail'),
)

