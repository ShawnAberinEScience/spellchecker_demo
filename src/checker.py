from collections import Counter
import numpy as np
from re import finditer,compile
from editdistpy import damerau_osa as ld
import pandas as pd
import nltk
from nltk import FreqDist as f_dist
from nltk.corpus import gutenberg as cor_g
import re 
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
		#dowload corpus
		nltk.download('gutenburg')
		nltk.corpus.gutenberg.fileids()
		corpus = Counter()
		for filename in nltk.corpus.gutenberg.fileids():
			words = [word.lower() for word in nltk.corpus.gutenberg.words(filename)]
			corpus.update(words)
		
		#corpus to df
		df = pd.DataFrame.from_dict(corpus, orient='index').reset_index()
		df = df.rename(columns={'index':'word', 0:'count'})

		words = gut.words(id in gut.fileids())
		p = f_dist(word.lower() for word in words)
			
    #use gutenberg corpus
    # turn the word and freq into df
		
class E_Model:
	
	def __init__(self,data:list[tuple[str,int]]):
		df = pd.DataFrame(data, columns=['error', 'count'])
		total = sum(df['count'])
		inv = 1/total
		df['p'] = df['count']*inv
		self.df = df
	
	#use regex to parse norvig's 1edit err
	letterPattern = r"[a-z|]+"
	numberPattern = r"\d+"

	file1 = open('count_1edit.txt', 'r')
	error_list = []
	counts = []
		
	for line in file1:
		letterMatch = re.findall(letterPattern, line)
		numberMatch = re.findall(numberPattern, line)
		error = letterMatch.pop(0)
		count = numberMatch.pop(0)
		error_list.append(error)
		counts.append(count)

