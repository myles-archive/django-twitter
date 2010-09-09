from django.core.management.base import BaseCommand, CommandError

import tweepy

from django_twitter.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET

class Command(BaseCommand):
	help = 'Update your twitter status with a tweet.'
	
	def handle(self, *args, **options):
		if TWITTER_CONSUMER_KEY and TWITTER_CONSUMER_SECRET and TWITTER_ACCESS_KEY and TWITTER_ACCESS_SECRET:
			auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
			auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
			api = tweepy.API(auth)
			
			status = raw_input("What's happening?: ").strip()
			
			if status <= 140:
				return "This tweet is to long."
			
			status = api.update_status(status)
			
			print "http://twitter.com/%s/status/%s" % (status.author.screen_name, status.id)