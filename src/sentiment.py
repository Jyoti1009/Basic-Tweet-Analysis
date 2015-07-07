import nltk
import csv
import pickle

import text_utils

'''
This file implements the code to train a sentiment classifier and test the same on new tweets. 
The Sentiment Classifier has been trained for approx. 7000 labeled tweets. The labels are 
	- positive
	- negative
	- neutral

The classifier is presently trained on English tweets. This is a very basic Sentiment Analysis code hence the
accuracy may be low.
'''

def read_csv(filename):
	# read the csv file and return the rows
	f = open(filename, 'rb')
	doc = csv.reader(f)
	rows = []
	for row in doc:
		rows.append(row)
	return rows

def get_trainingdata(rows):
	# return the tokenized form of tweets and it's sentiment for training the classifier
	datatable = []
	for sentiment,sentence in rows[1:]:
		datatable.append((get_tokens(sentence),sentiment))
	return datatable

def get_tokens(sentence):
	# return tokens of a tweet
	stopwords = text_utils.get_stopwords()
	sentence = text_utils.get_words(sentence, stopwords=stopwords)
	sentence = " ".join(sentence)
	tokens = nltk.tokenize.word_tokenize(sentence)
	bag_words = []
	for word in tokens:
		bag_words.append([word,'1'])
	return dict([i for i in bag_words])

def train_model(datatable):
	# Train the NaiveBayes Classifier of nltk module
	modelfile = open(get_model_filename(),'wb')
	classifier = nltk.NaiveBayesClassifier.train(datatable)
	pickle.dump(classifier,modelfile)
	modelfile.close()

def test_model(sentence,classifier):
	# Test the classifier model on new tweets
	tokens = get_tokens(sentence)
	prediction = classifier.classify(tokens)
	return prediction

def get_model():
	# Load the classifier model into memory
	modelfile = get_model_filename()
	model = open(modelfile)
	classifier = pickle.load(model)
	return classifier

def get_sentiments(tweets):
	sentiments = []
	classifier = get_model()
	for tweet in tweets:
		try:
			tweet = tweet.encode('ascii','ignore')
		except:
			tweet = tweet.decode('ascii','ignore')
		sentiment = test_model(tweet, classifier)
		sentiments.append((tweet,sentiment))
	return sentiments

def get_training_data_filename():
	# training data in csv format [Tweet, Sentiment]
	return './essentials/sentiment_analysis/trainingdata.csv'

def get_model_filename():
	return './essentials/sentiment_analysis/SentimentClassifier.model'
