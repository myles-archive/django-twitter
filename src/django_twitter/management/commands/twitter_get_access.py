from django.core.management.base import BaseCommand, CommandError

import tweepy

from django_twitter.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET

class Command(BaseCommand):
	help = 'Get the Twitter Access Key & Secret.'
	
	def handle(self, *args, **options):
		if TWITTER_ACCESS_KEY and TWITTER_ACCESS_SECRET:
			print "You already have a twitter access setup."
		else:
			if TWITTER_CONSUMER_KEY and TWITTER_CONSUMER_SECRET:
				auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
				auth_url = auth.get_authorization_url()
				print 'Please authorize: %s' % auth_url
				verifier = raw_input('PIN: ').strip()
				auth.get_access_token(verifier)
				print "Please add the following to your Django settings:"
				print "TWITTER_ACCESS_KEY = '%s'" % auth.access_token.key
				print "TWITTER_ACESSS_SECRET = '%s'" % auth.access_token.secret
			else:
				print "Please register your application at <http://twitter.com/oauth_clients>."
				print "Then fill in the 'TWITTER_CONSUMER_KEY' & 'TWITTER_CONSUMER_SECRET'."