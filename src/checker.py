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



from collections import namedtuple as ntu
import pandas
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
		if query.exists:
			return [tok]
		else:
			return getDist(tok)
