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

#### Code Structure
There are 6 codes in the ./src folder:
  - **text_utils.py**: This library contains the reusable modules for text processing
  - **twitter_utils.py**: This library contains the reusable modules for twitter API
  - **sentiment.py**: This library contains the reusable modules for training and testing sentiment analysis. To train a new model, put the training data in the given format (refer the code for more details) as */essentials/sentiment_analysis/trainingdata.csv*
  - **words_tweeted.py**: This script calculates total number of times each word has been tweeted and saves it as ./tweet_output/ft1.py
  - **median_unique.py**: This script calculates median number of unique words per tweet, and update this median as tweets come in and saves the result as ./tweet_output/ft2.py
  - **extra_features.py**: This script executes all other extra features and outputs different files in the folder ./tweet_output (Please refer code for more details)

#### Running the code
Run the *run.sh* file to execute the code. 
Currently the file executes only the two main features that are **words_tweeted.py** and **median_unique.py**. 

There are 4 ways to get the input tweets:
  - Stored tweets in ./tweets_input/tweets.txt file (**./tweets_input/tweets.txt**)
  - Get the twitter authorized user's homepage timeline of top 20 tweets (**twitter:home**)
  - Get the top 20 statuses update of the twitter authorized user (**twitter:none**)
  - Get the top 20 statuses update of any twitter user by the user_id (**twitter:[userid]**)

For the last 3 ways, twitter authorization must be done as explained above.
To run the extra features, all the dependencies must be first met. 

###### Running the extra features/twitter input
As mentioned above, there are three executable scripts *words_tweeted.py*, *median_unique.py* and *extra_features.py*.
These three executables can have 4 input variants as mentioned above. 
Hence, in *run.sh* file, there are three blocks separated by blank lines with each block containing 4 lines. These 4 lines have different input modes (refer to the brackets in 4 ways to get the input tweets above). Uncomment the lines that you want to run in *run.sh* and save and run!!

