#!/usr/bin/python

import sys
import json
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

#set the path to the input file
#tweets_data_path = 'C:/Users/Tanvi/Desktop/project2/stream/tweets_MH.txt'
tweets_data_path = 'C:/Users/Tanvi/Desktop/project2/stream/pollution/tweets_P.txt'



#open the input file for reading
tweets_file = open(tweets_data_path, "r")


#process each line in input file
for line in tweets_file:
    try:
        tweet = json.loads(line)
        word_list = []
        data = tweet['text'].strip().split(" ")   
        for i in range(len(data)):
            if len(data[i]) > 4:
                if ((data[i][0] == "#") or (data[i][0] == "@") or (data[i][:4]=="http")):
                    continue            
                else:
                    word_list.append(data[i].lower())
        filtered_words = [word for word in word_list if word not in stopwords.words('english')]

        if len(filtered_words) > 0:
            for i in range(len(filtered_words)):
                print ("{0}\t{1}".format(filtered_words[i], 1))
                
    except:
        continue
        

