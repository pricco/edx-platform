"""
URLs for track app
"""

from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = (
    'track.views',

    url(r'^event$', 'user_track'),
    url(r'^event/identify$', 'user_identify_event'),
    url(r'^event/page$', 'user_page_event'),
    url(r'^event/track', 'user_track_event'),
    url(r'^segmentio/event$', 'segmentio.segmentio_event'),
)

if settings.FEATURES.get('ENABLE_SQL_TRACKING_LOGS'):
    urlpatterns += (
        url(r'^event_logs$', 'view_tracking_log'),
        url(r'^event_logs/(?P<args>.+)$', 'view_tracking_log'),
    )

urlpatterns = patterns(*urlpatterns)
