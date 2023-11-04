# ---
# jupyter:
#   jupytext:
#\t cell_metadata_filter: -all
#\t formats: ipynb,py
#\t text_representation:
#\t   extension: .py
#\t   format_name: light
#\t   format_version: '1.5'
#\t   jupytext_version: 1.15.2
#   kernelspec:
#\t display_name: Python 3 (ipykernel)
#\t language: python
#\t name: python3
# ---

# steps:
# 1. get edit dist if using editdistpy, set max dist to 2*max(len(noisy),len(word))
# 2. get top k min edit dist
# 3. get top p max p of n-gram among k
# 4. find first probability of 1st error 
# 5. multiply to p


from collections import Counter
import numpy as np
from re import finditer,compile
from editdistpy import damerau_osa as ld
import pandas as pd
import nltk
from nltk import FreqDist as f_dist
from nltk.corpus import gutenberg as cor_g
# todo use faster dam-lev


class Finder:
	def __init__(self,err):

		self.model = L_Model()
	
		if not isinstance(err,pd.DataFrame):
			err = pd.DataFrame(err)
		self.err = err
			
	def getD(self,tok:str):
		candidates = []
		d = 1
		MAX = 90 #magic number set to the longest possible edit distance
		while not candidates and d <= MAX:
			candidates = [w for w in self.model.index if ld.distance(tok,w,d) > -1]
			d+=1
		return candidates
	
	def getCandidates(self,tok:str):
		candidates = [tok]
		if tok not in self.model:
			candidates = self.getD(tok)
			p_c =self.model[candidates]
			candidates = self.refine(p_c)
		return candidates
class L_Model:
	def __init__(self):
		words = gut.words(id in gut.fileids())
		p = f_dist(word.lower() for word in words)
			
    #use gutenberg corpus
    # turn the word and freq into df
		


class E_Model:
	#TODO use regex to parse norvig's 1edit err
	def __init__(self,data:list[tuple[str,int]]):
		df = pd.DataFrame(data, columns=['error', 'count'])
		total = sum(df['count'])
		inv = 1/total
		df['p'] = df['count']*inv
		self.df = df
