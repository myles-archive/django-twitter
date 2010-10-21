from django.core.management.base import BaseCommand, CommandError

from django_twitter import utils

class Command(BaseCommand):
	help = 'Check to see if everything is working okay.'
	
	def handle(self, *args, **options):
		api = utils.auth()
		
		if api:
			return api.test()