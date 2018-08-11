#!/usr/bin/python

import sys
import json

#set the path to the input file
tweets_data_path = 'C:/Users/Tanvi/Desktop/project2/stream/tweets_MH.txt'
#tweets_data_path = 'C:/Users/Tanvi/Desktop/project2/stream/pollution/tweets_P.txt'

#initialize an array and open the output file for reading
tweets_file = open(tweets_data_path, "r")


#process each line in input file
for line in tweets_file:
    try:
        tweet = json.loads(line)
        num_urls = len(tweet['entities']['urls'])
        #print("num_urls: ", num_urls)
        if num_urls > 0:
            for i in range(num_urls):
                url = tweet['entities']['urls'][i]["expanded_url"]
                if url:
                    print ("{}\t{}".format(url.lower(), 1))
                else:
                    url = tweet['entities']['urls'][i]["url"]
                    if url:
                        print ("{}\t{}".format(url.lower(), 1))        
                
    except:
        continue
    

