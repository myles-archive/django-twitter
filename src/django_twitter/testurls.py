from django.contrib import admin
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/twitter/', include('django_twitter.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/(.*)', admin.site.root),
)
