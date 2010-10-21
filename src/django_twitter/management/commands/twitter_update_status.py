import logging

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from django_twitter import utils

log = logging.getLogger("django_twitter.management.commands.twitter_update_status")

class Command(BaseCommand):
	help = 'Update your twitter status with a tweet.'
	
	def handle(self, *args, **options):
		level = { '0': logging.WARN, '1': logging.INFO, '2': logging.DEBUG }[options.get('verbosity', '0')]
		logging.basicConfig(level=level, format="%(name)s: %(levelname)s: %(message)s")
		
		api = utils.auth()
		
		if api:
			status = raw_input("What's happening?: ").strip()
			
			if len(status) > 140:
				return log.warn("This tweet is to long. It has %s charaters.", len(status))
			
			if not settings.DEBUG:
				status = api.update_status(status)
				log.info("http://twitter.com/%s/status/%s" % (status.author.screen_name, status.id))
			else:
				return log.debug(status)