from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
import json
import re
import time
import re
from tweepy import Stream
from tweepy.streaming import StreamListener

def percentage(gained , total):
   return ((float(gained)/float(total))*100)

consumer_key = '***********'
consumer_secret = '**********************************************'
access_token = '*************************************************'
access_token_secret = '********************************************'
 
auth = tweepy.OAuthHandler(consumer_key=consumer_key,consumer_secret = consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

searchterm = input("Enter the keyword to search:")
Nooftweets = input("Enter the number of tweets ")
tweets =tweepy.Cursor(api.search , q=searchterm , lang ="English").items(200)

positive = 0
negative = 0
neutral = 0
polarity = 0 

for tweet in tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	polarity = analysis.sentiment.polarity
	print(polarity)
	if(polarity == 0):
		neutral = neutral + 1
	elif(polarity > 0.00):
		positive = positive + 1
	elif(polarity < 0.00):
		negative = negative + 1

positive = percentage(positive , Nooftweets)
negative = percentage(negative , Nooftweets)
neutral = percentage(neutral , Nooftweets)

positive = format(positive , '.2f')
negative = format(negative , '.2f')
neutral = format(neutral , '.2f')

labels = ['Positive['+str(positive)+'%]','Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]']

sizes = [positive , neutral , negative]
colors = ['yellow' ,'green' , 'red']
patches , texts = plt.pie(sizes , colors=colors , startangle=90)
plt.legend(patches , labels , loc='best')
plt.title("Analysis")
plt.axis('equal')
plt.tight_layout()
plt.show()





