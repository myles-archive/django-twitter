from django import forms
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.admin.widgets import AdminTextareaWidget

from django_twitter import utils

class TweetForm(forms.Form):
	tweet = forms.CharField(max_length=400, widget=AdminTextareaWidget)

@staff_member_required
def home(request):
	context = {
		'title': 'Twitter',
	}
	return render_to_response('django_twitter/home.html', context, context_instance=RequestContext(request))

@staff_member_required
@cache_page(60 * 15)
def timeline(request):
	"""
	Twitter timeline page.
	"""
	api = utils.auth()
	
	if api:
		tweets = api.friends_timeline()
	else:
		tweets = None
	
	context = {
		'tweets': tweets,
		'title': 'Twitter Timeline',
	}
	
	return render_to_response('django_twitter/timeline.html', context, context_instance=RequestContext(request))

@staff_member_required
def tweet(request):
	context = {
		'title': 'Twitter',
		'form': TweetForm(),
	}
	return render_to_response('django_twitter/tweet.html', context, context_instance=RequestContext(request))