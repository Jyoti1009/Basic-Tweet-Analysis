import csv
import time

import text_utils as txu
import twitter_utils as twu
import sentiment as st 

'''
This file implements a few extra features like:
		- extracting all URLs in the tweets
		- extracting all hashtags in the tweets
		- extracting all replyats in the tweets
		- get sentiment for each tweet
		- get worldwide trending hashtags

'''

def write_csv(data, filename):
	with open(filename, 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(data)

if __name__ == '__main__':
	# get path for all outputs
	inp, urls, tags, replyats, sentiment, trends = txu.extract_arguments(n=7)
	tweets = twu.get_input(inp)
	tweets_text = "\n".join(tweets)	
	
	# extract all URLs in the tweets and write in a file
	start = time.clock()
	txu.write_file('\n'.join(txu.get_urls(tweets_text)), urls)
	print "Time taken in extracting URLs: ", time.clock() - start

	# extract all hashtags in the tweets and write in a file
	start = time.clock()
	txu.write_file('\n'.join(txu.extract_hashtags(tweets_text)), tags)
	print "Time taken in extracting hashtags: ", time.clock() - start

	# extract all replyats in the tweets and write in a file
	start = time.clock()
	txu.write_file('\n'.join(txu.extract_replyat(tweets_text)), replyats)
	print "Time taken in extracting replyats: ", time.clock() - start

	# get sentiments in the tweets and write in a file
	start = time.clock()
	write_csv(st.get_sentiments(tweets), sentiment)
	print "Time taken in extracting sentiment: ", time.clock() - start

	# extract all trending hashtags worldwide and write in a file
	start = time.clock()
	txu.write_file('\n'.join(twu.get_worldwide_trends()), trends)
	print "Time taken in extracting trends: ", time.clock() - start
	
