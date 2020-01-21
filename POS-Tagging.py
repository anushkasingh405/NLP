##############ex.3
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
filename='NLPdataEx3&4-data_in.txt'
file = open(filename, "r")
data= file.read()
##########tokenizing
words = word_tokenize(data)
######pos-tagging
tokens_tag = pos_tag(words)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp  =nltk.RegexpParser(grammar)
result = cp.parse(tokens_tag)
result.draw()
