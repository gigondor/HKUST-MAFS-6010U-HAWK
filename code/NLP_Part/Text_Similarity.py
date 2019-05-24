# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:37:34 2019

@author: yyeam
"""

import nltk
# NLTK has a built-in function
# to check Levenshtein distance:
from nltk.metrics import edit_distance

def print_levenshtein(string1, string2):
  print("The Levenshtein distance from '{0}' to '{1}' is {2}!".format(string1, string2, edit_distance(string1, string2)))

# Check the distance between
# any two words here!
print_levenshtein("fart", "target")

# Assign passing strings here:
three_away_from_code = "cadra"

two_away_from_chunk = "chunig"

print_levenshtein("code", three_away_from_code)
print_levenshtein("chunk", two_away_from_chunk)