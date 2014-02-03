from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render_to_response

import urllib
import json

from pyteaser import SummarizeUrl
from twitter_api import api

def index(request):
	max_count = 100
	timeline = api.statuses.home_timeline(count=max_count)
	tweets_with_links = [tweet for tweet in timeline if tweet['entities']['urls']]

	for tweet in tweets_with_links:
		tweet['oembed'] = oembed(tweet)

	response = { 'timeline': tweets_with_links }
	return render_to_response('app/index.html', response)


def summarize(request, url):
	decoded_url = urllib.unquote(url).decode('utf8')
	if cache.get(decoded_url):
		return HttpResponse(cache.get(decoded_url))
	else:
		summaryList = SummarizeUrl(decoded_url)
		summary = '|'.join(summaryList)
		cache.set(decoded_url, summary, 15*60) 	# keep in cache for 15 mins
		return HttpResponse(summary)


def oembed(tweet):
	cache_key = str(tweet['id'])
	if cache.get(cache_key):
		return cache.get(cache_key)
	else:
		oembed = api.statuses.oembed(_id=tweet['id'], omit_script='true')
		oembed['html'] = oembed['html'].rstrip()
		cache.set(cache_key, dict(oembed), 15*60)	# keep in cache for 15 mins
		return oembed
