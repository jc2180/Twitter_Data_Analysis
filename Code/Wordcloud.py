#!/usr/bin/python

from wordcloud import WordCloud
import matplotlib.pyplot as plt

word_file = 'C:/Users/Tanvi/Desktop/project2/hashtag/sign_words_MH.txt'

#initialize an array and open the output file for reading
word_string = open(word_file, "r")

text = word_string.read()
wordcloud = WordCloud(background_color='white', width=1200, height=1000).generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
