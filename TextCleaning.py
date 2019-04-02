import nltk
import string
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
positive = 0
negative = 0
neutral = 0
polarity = 0 
comment =[]
def text_cleaning(filename):
	filename = filename+'.txt'
	data =data = pd.read_csv(filename, sep=" ")
	words=word_tokenize(data)
	punc = set(string.punctuation)
	stop_words = set(stopwords.words('english'))
	for w in words:
        	if w not in (punc , stop_words):
			analysis = TextBlob(w)
			polarity = analysis.sentiment.polarity
			if(polarity == 0):
				neutral = neutral + 1
				print (neutral)
			elif(polarity > 0.00):
				positive = positive + 1
				print (positive)
			elif(polarity < 0.00):
				negative = negative + 1
				print(negative)
filename='intern_test.py'
text_cleaning(filename)
