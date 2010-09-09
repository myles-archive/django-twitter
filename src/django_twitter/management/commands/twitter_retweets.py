from django.core.management.base import BaseCommand, CommandError

import tweepy

from django_twitter.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET

class Command(BaseCommand):
	help = 'Check to see what tweets have been retweeted.'
	
	def handle(self, *args, **options):
		if TWITTER_CONSUMER_KEY and TWITTER_CONSUMER_SECRET and TWITTER_ACCESS_KEY and TWITTER_ACCESS_SECRET:
			auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
			auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
			api = tweepy.API(auth)
			
			tweets = api.retweets_of_me()
			
			for tweet in tweets:
				print "%s:\t%s" % (tweet.id, tweet.text)