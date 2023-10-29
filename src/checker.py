# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:light
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



from collections import namedtuple as ntu, Counter
import numpy as np
from re import finditer,compile
from editdistpy import damerau_osa


#todo use dam-lev 0.1.2 instead 


class Finder:
	def __init__(model):
#model is the language model use pd df
		self.model = model
		self.query = ntu('Query', ['exists','val'])
	def queryModel(tok:str):
		exists = tok in self.model
		# TODO: check for instances
		val = model[tok] if exists else None
		return self.query(exists,val)
	

	def getD(tok:str):
		candidates = []
		max_d = 1
		sentinel = 45<<1 #magic number. set to twice the length of longest word in corpus
		while not (candidates or max_d > sentinel) :
			candidates = [word for word in self.model.keys() if damerau_osa.distance(tok,word,max_d) > -1]
			max_d += 1
		return candidates
	
	def getCandidates(tok:str):
		query = querModel
		candidates = []
		if query.exists:
			return [tok]
		else:
			candidates = self.getD(tok)
			p_c =[model[word] for word in candidates]
			weighted = list(zip(candidates,p_c))
			weighted.sort(key = lambda tu: tu[1],reversed = True)
			islong = len (weighted)>=n
			return weighted[::n] if islong else weighted
class L_Model:
#use pandas
	def __init__(self, corpus):
		isstr = instanceof(corpus,str)
		ispd = instanceof(corpus,pd.df)
		isctr = instanceof(corpus, Counter)
		if isstr:
			#use nltk to tokenize corpus then use counter
			for word in corpus:
				pass
				#count the occurence of word
		elif isctr:
			self.model = self.getP_C(coprus)
			#iterate corpus. create dict with probabilities
			#probably put this as nother func. isstr may need this

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
