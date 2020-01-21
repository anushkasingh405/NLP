###########ex.4
import nltk
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
filename='NLPdataEx3&4-data_in.txt'
file = open(filename, "r")
data= file.read()
##########tokenizing
words = word_tokenize(data)
stop_words = set(stopwords.words('english'))
punc = set(string.punctuation)
comment =[]
stem_sentence=[]
lemma=[]
porter = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
for w in words:
    if w not in punc and w not in stop_words:
        comment.append(w)
for word in comment:
    stem_sentence.append(porter.stem(word))
    lemma.append(wordnet_lemmatizer.lemmatize(word))
print("stem_sentence",stem_sentence)
print("lemma",lemma)
