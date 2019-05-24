# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:38:30 2019

@author: yyeam
"""

# Text Preprocessing
# regex for removing punctuation!
import re
# nltk preprocessing magic
import nltk
# from nltk.corpus import words
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize

from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer

from nltk.stem import WordNetLemmatizer

# import spacy

text = open("SensetimeEn.txt", "r").read()

cleaned = re.sub('\W+', ' ', text)
tokenized = word_tokenize(cleaned)

# 词干提取 （stemming）

porter_stemmer = PorterStemmer()
porter_stemmed = [porter_stemmer.stem(token) for token in tokenized] 

lancaster_stemmer = LancasterStemmer()
lancaster_stemmed = [lancaster_stemmer.stem(token) for token in tokenized]

snowball_stemmer = SnowballStemmer("english")
snowball_stemmed = [snowball_stemmer.stem(token) for token in tokenized]

# 词形还原 （lemmatization）
# Lemmatize with POS Tag
def get_wordnet_pos(word):
    # Map POS tag to first character lemmatize() accepts
    # a "part of speech" function
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

# Init Lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize the text we used with the appropriate POS tag
lemmatized=[lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in tokenized]

print("Original text:")
print(tokenized)
print("\nPorter Stemmed text:")
print(porter_stemmed)
print("\nLancaster Stemmed text:")
print(lancaster_stemmed)
print("\nSnowball Stemmed text:")
print(snowball_stemmed)
print("\nLemmatized text:")
print(lemmatized)