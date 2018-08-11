import sys
import json

#set the path to the output file
#tweets_data_path = 'C:/Users/Tanvi/Desktop/project2/stream/tweets_MH.txt'
tweets_data_path = 'C:/Users/Tanvi/Desktop/project2/stream/pollution/tweets_P.txt'

#initialize an array and open the output file for reading
tweets_data = []
tweets_file = open(tweets_data_path, "r")

#process each line in output file
for line in tweets_file:
    try:
        tweet = json.loads(line)
        retweet_id = tweet['retweeted_status']['id_str']
        if retweet_id:
            tweet_text = tweet['retweeted_status']['text']
            print ("{0}\t{1}\t{2}".format(retweet_id, 1, tweet_text))
    except:
        continue
        
