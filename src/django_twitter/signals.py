import logging

from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.conf import settings

from django_twitter import utils

log = logging.getLogger("django_twitter.signals")

def tweet(sender, instance, **kwargs):
	TOTAL_CHARS = 140
	
	api = utils.auth()
	
	if api:
		ctype = ContentType.objects.get_for_model(instance)
		
		template_list = [
			"django_twitter/snippets/%s.html",
			"django_twitter/snippets/item.html"
		]
		
		context = { 'obj': instance }
		
		tweet = render_to_string(template_list, context)
		
		if instance.get_absolute_url():
			site = Site.objects.get_current()
			url = "http://%s%s" % (site.domain, instance.get_absolute_url())
			url_length = len(url) + len(': ')
			TOTAL_CHARS = TOTAL_CHARS - url_length
		
		if len(tweet) >= TOTAL_CHARS:
			TOTAL_CHARS = TOTAL_CHARS - len('...')
			tweet = ' '.join(tweet[:TOTAL_CHARS].split(' ')[:-1]) + '...'
		
		if url:
			tweet += ': ' + url
		
		if not settings.DEBUG:
			return api.update_status(tweet)
		else:
			return log.debug(tweet)