import tweepy
import json
import pprint
import time

import text_utils

# authorize and access Twitter API
path = './essentials/twitter_credentials/access.json'
json_data = text_utils.read_file(path)
credentials = json.loads(json_data)
auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
api = tweepy.API(auth)

def get_home_timeline():
	# returns top 20 tweets on your homepage
	public_tweets = api.home_timeline()
	tweets = []
	for tweet in public_tweets:
	    tweets.append(tweet.text)
	return tweets

def get_tweets_of(user=None):
	# returns the top 20 tweets of any user given the user id
	if user == None:
		public_tweets = api.user_timeline()
	else:
		public_tweets = api.user_timeline(user)
	tweets = []
	for tweet in public_tweets:
	    tweets.append(tweet.text)
	return tweets

def get_worldwide_trends():
	# returns top worldwide trending topics
	location = 1 # woeid of worldwide is 1 on twitter
	trending_topics = api.trends_place(location)
	trends = []
	topic_dict = trending_topics[0]
	for trend in topic_dict['trends']:
		trends.append(trend['name'])
	return trends
		
def get_available_trends():
	# returns a dictionary of trending topics locationwise. 
	'''This function hits the API for quite a large number of times. 
	Hence it will take time to execute due to API rate limit.'''
	trends_data = api.trends_available()
	locations = []

	# extracts all locations of trends
	for location in trends_data:
		locations.append((location['woeid'],location['name']))
	
	trends = {}
	# extracts the topics for each location
	for loc_id, loc_name in locations:
		trending_topics = api.trends_place(loc_id)
		time.sleep(70)                   # regulates the api hits 
		trends[loc_name] = []
		topic_dict = trending_topics[0]
		for trend in topic_dict['trends']:
			trends[loc_name].append(trend['name'])
	return trends

def get_input(inp):
	# returns the tweets on the basis of provided input
	try:
		tinp = inp.split(':')
		mode = tinp[0]
		usr = tinp[1]
	except:
		pass
	if mode == 'twitter':
		if usr == 'home':
			tweets = get_home_timeline()	    # get tweets from twitter homepage
		elif usr == 'none':
			tweets = get_tweets_of()			# get tweets of the authorized api account
		else:
			tweets = get_tweets_of(usr)			# get tweets of any usr by his userid
	else:
		tweets = text_utils.read_file(inp).split('\n')

	return tweets

	