from django.core.management.base import BaseCommand, CommandError

import tweepy

from django_twitter.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET

class Command(BaseCommand):
	help = 'Search twitter.'
	
	def handle(self, *args, **options):
		if TWITTER_CONSUMER_KEY and TWITTER_CONSUMER_SECRET and TWITTER_ACCESS_KEY and TWITTER_ACCESS_SECRET:
			auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
			auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
			api = tweepy.API(auth)
			
			query = raw_input('Query: ').split()
			
			results = api.search(query)
			
			for result in results:
				print "\n%s" % result.text
				print "\t@%s - %s" % (result.from_user, result.created_at)
				print "\thttp://twitter.com/%s/status/%s" % (result.from_user, result.id)