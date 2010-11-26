from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

urlpatterns = patterns('',
	# Example:
	# (r'^project_template/', include('project_template.foo.urls')),
	
	(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root':getattr(settings,'MEDIA_ROOT')}),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout')
)
