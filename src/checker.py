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


import pandas
from editdistpy import damerau_osa
class Checker:
	def __init__(model):
#model is the language model use pd df
		self.model = model
	def getDist(tok:str):
		tok_l = len(tok)
		max_dist = tok_l
		candidates = []
		empty = true
		max_d = 1
		while empty:
			candidates = [word for word in self.model.keys() if damerau_osa.distance(tok,word,max_d) > -1]
			#change line directly above to df.apply
			#get list of keys with dist greater than sentinel
			empty,max_d = (False, max_d) if candidates else (True, max_d+1)
			
