# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:52:03 2019

@author: yyeam
"""

# for this program, please use colab to run it

import spacy
from nltk import Tree

text = '''So many squids are jumping out of suitcases these days that you can 
barely go anywhere without seeing one burst forth from a tightly packed valise. 
I went to the dentist the other day, and sure enough I saw an angry one jump 
out of my dentist's bag within minutes of arriving. She hardly even noticed.'''

dependency_parser = spacy.load('en')

parsed_text = dependency_parser(text)

def to_nltk_tree(node):
  if node.n_lefts + node.n_rights > 0:
    parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
    return Tree(node.orth_, parsed_child_nodes)
  else:
    return node.orth_

for sent in parsed_text.sents:
  to_nltk_tree(sent.root).pretty_print()