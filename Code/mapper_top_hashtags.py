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
        num_tags = len(tweet['entities']['hashtags'])        
        if num_tags > 0:
             for i in range(num_tags):
                tag = tweet['entities']['hashtags'][i]['text']
                if tag:
                    print ("{}\t{}".format(tag.lower(), 1))
        else:
             data = tweet['text'].strip().split(" ")
             for i in range(len(data)):
                  if len(data[i]) > 0:
                       if data[i][0]=="#":
                            print ("{0}\t{1}".format(data[i].lower(), 1))
     
     except:
          continue
    
    
                
            
