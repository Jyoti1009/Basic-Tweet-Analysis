#!/bin/bash

python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
# python ./src/words_tweeted.py twitter:home ./tweet_output/ft1.txt
# python ./src/words_tweeted.py twitter:none ./tweet_output/ft1.txt
# python ./src/words_tweeted.py twitter:<userid> ./tweet_output/ft1.txt

python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt
# python ./src/median_unique.py twitter:home ./tweet_output/ft2.txt
# python ./src/median_unique.py twitter:none ./tweet_output/ft2.txt
# python ./src/median_unique.py twitter:<userid> ./tweet_output/ft2.txt

python ./src/extra_features.py ./tweet_input/tweets.txt ./tweet_output/urls.txt ./tweet_output/hashtags.txt ./tweet_output/replyats.txt ./tweet_output/sentiment.csv ./tweet_output/trends.txt
# python ./src/extra_features.py twitter:home ./tweet_output/urls.txt ./tweet_output/hashtags.txt ./tweet_output/replyats.txt ./tweet_output/sentiment.csv ./tweet_output/trends.txt
# python ./src/extra_features.py twitter:none ./tweet_output/urls.txt ./tweet_output/hashtags.txt ./tweet_output/replyats.txt ./tweet_output/sentiment.csv ./tweet_output/trends.txt
# python ./src/extra_features.py twitter:<userid> ./tweet_output/urls.txt ./tweet_output/hashtags.txt ./tweet_output/replyats.txt ./tweet_output/sentiment.csv ./tweet_output/trends.txt

