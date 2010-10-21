from django.core.management.base import BaseCommand, CommandError

from django_twitter import utils

class Command(BaseCommand):
	help = 'Search twitter.'
	
	def handle(self, *args, **options):
		api = utils.auth()
		
		if api:
			query = raw_input('Query: ').split()
			
			results = api.search(query)
			
			for result in results:
				print "\n%s" % result.text
				print "\t@%s - %s" % (result.from_user, result.created_at)
				print "\thttp://twitter.com/%s/status/%s" % (result.from_user, result.id)