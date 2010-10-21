import logging

import tweepy

from django_twitter.settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET

log = logging.getLogger("django_twitter.utils")

def auth():
	if TWITTER_CONSUMER_KEY and TWITTER_CONSUMER_SECRET and TWITTER_ACCESS_KEY and TWITTER_ACCESS_SECRET:
		auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
		auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
		api = tweepy.API(auth)
		return api
	else:
		log.debug("Please enter your TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, and TWITTER_ACCESS_SECRET in your settings file.")
		return False