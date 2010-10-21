DEBUG = True
DEBUG_TEMPLATE = True
SITE_ID = 1
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/django-twitter-devel.db'
INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.admindocs',
	
	'django_twitter',
]
ROOT_URLCONF = 'django_twitter.testurls'

try:
	from django_twitter.localsettings import *
except ImportError:
	pass