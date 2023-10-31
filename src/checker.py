# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# steps:
# 1. get edit dist if using editdistpy, set max dist to 2*max(len(noisy),len(word))
# 2. get top k min edit dist
# 3. get top p max p of n-gram among k



from collections import Counter
import numpy as np
from re import finditer,compile
from editdistpy import damerau_osa as ld
import pandas as pd

# todo use dam-lev 0.1.2 instead 


class Finder:
	def __init__(model,err):
#model is the language model use pd df
		if not isinstance(model,pd.DataFrame):
			model = pd.DataFrame(model)
		self.model = model
		if not isinstance(err,pd.DataFrame):
			err = pd.DataFrame(err)
		self.err = err
			
	def getD(tok:str):
		candidates = []
		d = 0
		max = 90 #magic number set to the longest possible edit distance
		while not candidates and d < max:
			d+=1
			candidates = [w for w in self.model.index if ld.distance(tok,w,d) > -1]
		return candidates
	
	def getCandidates(tok:str):
		candidates = [tok]
		if tok not in self.model:
			candidates = self.getD(tok)
			p_c =self.model[candidates]
			candidates = self.refine(p_c)
		return candidates
class L_Model:
	def __init__(self, corpus):
		isstr = instanceof(corpus,str)
		ispd = instanceof(corpus,pd.df)
		isctr = instanceof(corpus, Counter)
		if isstr:
			#use nltk to tokenize corpus then use counter
			for word in corpus:
				pass
		elif isctr:
			self.model = self.getP_C(coprus)


	def getP_C(self,counts):
		total = sum(counts.values())
		r_t = 1/total
		keys = counts.keys()
		vals = np.array(counts.values())/r_t
		return dict(zip(keys,vals))


class E_Model:
	#TODO use regex to parse norvig's 1edit err
	def __init__(self,data:list[tuple[str,int]]):
		df = pd.DataFrame(data, columns=['error', 'count'])
		total = sum(df['count'])
		inv = 1/total
		df['p'] = df['count']*inv
		self.df = df
