# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:01:01 2019

@author: yyeam
"""

import nltk, re
from nltk.tokenize import word_tokenize
# importing ngrams module from nltk
from nltk.util import ngrams
from collections import Counter

text = open("SensetimeEn.txt", "r").read()

cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)

# Change the n value to 2:
bigrams = ngrams(tokenized, 2)
bigrams_frequency = Counter(bigrams)

# Change the n value to 3:
trigrams = ngrams(tokenized, 3)
trigrams_frequency = Counter(trigrams)

# Change the n value to a number greater than 3:
ngrams = ngrams(tokenized, 5)
ngrams_frequency = Counter(ngrams)

print("Bigrams:")
print(bigrams_frequency.most_common(10))

print("\nTrigrams:")
print(trigrams_frequency.most_common(10))

print("\nN-grams:")
print(ngrams_frequency.most_common(10))