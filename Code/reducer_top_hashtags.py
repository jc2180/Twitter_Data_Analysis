#!/usr/bin/python

import sys
import operator

tweets_data = dict()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisTag, thisCount = data_mapped

    if thisTag in tweets_data.keys():
        tweets_data[thisTag] += int(thisCount)
    else:
        if len(tweets_data) > 10:
            min_key = min(tweets_data, key=tweets_data.get)
            tweets_data.pop(min_key)
            tweets_data[thisTag] = int(thisCount)
        else:
            tweets_data[thisTag] = int(thisCount)
            
    
sorted_tweet = sorted(tweets_data.items(), key=operator.itemgetter(1), reverse = True)[0:10]

for data in sorted_tweet:
    print ("{0}\t{1}".format(data[0], data[1]))

