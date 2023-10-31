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
	def __init__(lang,err):
#model is the language model use pd df
		self.lang = lang
		self.query = ntu('Query', ['exists','val'])
		self.err = err
	def queryModel(tok:str):
		exists = tok in self.model
		# TODO: check for instances
		val = model[tok] if exists else None
		return self.query(exists,val)
	

	def getD(tok:str):
		candidates = []
		max_d = 0
		sentinel = 45<<1 #magic number. set to twice the length of longest word in corpus
		while not candidates and max_d < sentinel :
			max_d+=1
			candidates = [word for word in self.lang if damerau_osa.distance(tok,word,max_d) > 0]
			
		return candidates
	
	def getCandidates(tok:str):
		query = querModel
		candidates = []
		if query.exists:
			return [tok]
		#what calls this checks if tok is in the return value
		else:
			candidates = self.getD(tok)
			p_c = self.lang[candidates]

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
			for word in lang:
			
		elif isdict:
			self.model = self.getP_C(coprus)
			#iterate corpus. create dict with probabilities


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
