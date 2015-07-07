import logging
import os
import sys
import re
import string
import collections

def extract_arguments(n=3):
	'''
	This function examines the command-line arguments and returns the input file
	and output file as provided on command-line
	'''
	# check and process input arguments
	if len(sys.argv) < 3:
		print globals()['__doc__'] % locals()
		sys.exit(1)
	if n==7:
		inp, out_url, out_tag, out_rply, out_st, out_trend = sys.argv[1:7]
		return inp, out_url, out_tag, out_rply, out_st, out_trend
	else:
		inp, outp = sys.argv[1:3]
		return inp, outp

def get_urls(text):
	# return all valid urls in a piece of text
	return re.findall(r'(https?://\S+)', text)

def get_words(text, stopwords=None):
	'''
	This function removes the urls and unimportant words (if stopwords!=None) 
	and performs other preprocessing
	'''
	# remove urls
	urls = get_urls(text)	
	text = preprocess_text(text)
	text = text.split()
	text = ' '.join(item for item in text if item not in urls)

	# remove stopwords
	if stopwords != None:
		stopwords = stopwords.split()
		text = text.split()
		text = ' '.join(item for item in text if item not in stopwords)

	# return words in text
	return text.split()

def extract_hashtags(text):
	# return the hashtags used in text
	text = preprocess_text(text)
	text = text.split()
	hashtags = [word for word in text if word[0] == '#']
	return hashtags

def extract_replyat(text):
	# return the hashtags used in text
	text = preprocess_text(text)
	text = text.split()
	replyat = [word for word in text if word[0] == '@']
	return replyat

def preprocess_text(text):
	# cleans the text of invalid and insignificant characters
	text = text.replace('\n', ' ')
	text = text.replace('\t', ' ')
	text = text.lower()
	# remove punctuations except # and @ as they are significant
	exclude = set(string.punctuation)
	exception = set(['@','#'])
	exclude -= exception
	text = ''.join(ch for ch in text if ch not in exclude)
	try:
		text = text.decode('ascii','ignore')
	except:
		text = text.encode('ascii','ignore')
	return text

def extract_words(text):
	# returns all the words separated by whitespaces and includes urls and stopwords
	text = preprocess_text(text)
	words = get_words(text)
	urls = get_urls(text)
	return words + urls

def read_file(filename):
	# return text in a file
	return open(filename,'r').read()

def write_file(data, filename):
	# write data in file
	try:
		data = data.encode('ascii','ignore')
	except:
		data = data.decode('ascii','ignore')
	open(filename,'w').write(data)

def get_counter(wordlist):
	# return the counter of words and its occurrences
	return collections.Counter(wordlist)    

def get_noofunique(tweet):
	# returns number of unique words in a tweet
	text = preprocess_text(tweet)
	text = text.split()
	return len(set(text))

def get_median_iterative(tweet, median_dict):
	# update an return new median dictionary containing median and number of tweets with incoming tweet
	word_length = get_noofunique(tweet) # get the number of unique words in the tweet
	length = median_dict['length']
	length_new = length + 1
	sum_original = median_dict['median'] * length
	sum_new = sum_original + word_length

	# calculate median
	median_new = float(sum_new) / length_new

	median_dict['median'] = median_new
	median_dict['length'] = length_new
	return median_dict

def get_stopwords():
	# return stopwords
	path = './essentials/stopwords/stopwords.txt'
	return read_file(path)

