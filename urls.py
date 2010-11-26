from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
	(r'', include('sentry.urls')),
	(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root':getattr(settings,'MEDIA_ROOT')}),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout')
)
