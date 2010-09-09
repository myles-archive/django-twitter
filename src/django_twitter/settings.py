from django.conf import settings

TWITTER_CONSUMER_KEY = getattr(settings, 'TWITTER_CONSUMER_KEY', None)
TWITTER_CONSUMER_SECRET = getattr(settings, 'TWITTER_CONSUMER_SECRET', None)

TWITTER_ACCESS_KEY = getattr(settings, 'TWITTER_ACCESS_KEY', None)
TWITTER_ACCESS_SECRET = getattr(settings, 'TWITTER_ACCESS_SECRET', None)