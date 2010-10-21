from django.conf.urls.defaults import *

urlpatterns = patterns('django_twitter.views',
	url(r'^tweet/',
		view = 'tweet',
		name = 'django_twitter_tweet'
	),
	url(r'^timeline/$',
		view = 'timeline',
		name = 'django_twitter_timeline'
	),
	url(r'^$',
		view = 'home',
		name = 'django_twitter_home'
	),
)