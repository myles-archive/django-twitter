from django.core.management.base import BaseCommand, CommandError

from django_twitter import utils

class Command(BaseCommand):
	help = 'Check to see what tweets have been retweeted.'
	
	def handle(self, *args, **options):
		api = utils.auth()
		
		if api:
			tweets = api.retweets_of_me()
			
			for tweet in tweets:
				print "%s:\t%s" % (tweet.id, tweet.text)