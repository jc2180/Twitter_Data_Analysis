#!/usr/bin/python

import sys
import operator

tweets_data = dict()
tweets_text = dict()


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    thisID, thisCount, thisText = data_mapped

    if thisID in tweets_data.keys():
        tweets_data[thisID] += int(thisCount)        
    else:
        if len(tweets_data) > 10:
            min_key = min(tweets_data, key=tweets_data.get)
            tweets_data.pop(min_key)
            tweets_data[thisID] = int(thisCount)
            tweets_text.pop(min_key)
            tweets_text[thisID] = thisText
        else:
            tweets_data[thisID] = int(thisCount)
            tweets_text[thisID] = thisText

sorted_tweet = sorted(tweets_data.items(), key=operator.itemgetter(1), reverse = True)[0:10]

for data in sorted_tweet:
    tweet_text = tweets_text[data[0]]
    print ("{0}\t{1}".format(data[1], tweet_text))
