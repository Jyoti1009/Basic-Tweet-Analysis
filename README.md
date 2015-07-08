# Insight Data Engineering Assignment

### Introduction

The code is an implementation of few features which take tweets as input and extracts informations from the same.
The code is extremely modular and self explanatory with required comments.

#### Features Implemented

The two main features implemented are:
  - Total number of times each word has been tweeted.
  - Median number of unique words per tweet, and update this median as tweets come in.

The above features are mandatory features implemented.

The below features are extra features:
  - Extracts all URLs in the tweets
  - Extracts all hashtags in the tweets
  - Extracts all replyats in the tweets
  - Gets sentiment for each tweet
  - Gets worldwide trending hashtags
  - Gives the time taken to evaluate above results

#### Speed
This code has been tested on a tweet corpus more than 33000 tweets and gives the main features' output in a matter of split seconds.
The maximum time taken by a code is taken by sentiment prediction but even this is fast enough.  

#### Folder Structure
The folder structure image can be found in the folder images.
  - All the essentials required to run the code are provided in the ./essentials folder. This contains files like stopwords, sentiment classifier and twitter credentials.
  - All the codes are in the folder ./src
  - All the input files can be placed in the folder ./tweet_input
  - All the output files can be placed in the folder ./tweet_output

#### Dependencies
The code is written in python language on Python2.7 platform and hence needs the same version to be installed.
The below pointers give the libraries required for running the code smoothly for extra features
  * tweepy
  * nltk
  * nltk-data

Apart from the above library, provide the twitter authorization credentials in the file */essentials/twitter_credentials/access.json* to run the twitter API.

#### Running the code
Run the *run.sh* file to execute the code. 
Currently the file executes only the two main features that are **words_tweeted.py** and **median_unique.py**. 
There are 4 ways to get the input 

