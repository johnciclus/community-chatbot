import nltk
import numpy as np
import random
import string # to process standard python strings

f=open('chatbot.txt','r',errors = 'ignore')
raw=f.read()

#nltk.download('punkt')
#nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

print(word_tokens)