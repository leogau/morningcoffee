from twitter import *

from settings import *

api = Twitter(
	auth=OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, 
		CONSUMER_KEY, CONSUMER_SECRET)
)
