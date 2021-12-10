# author: Tamas Demian
# date: 2021-12-08

from string import ascii_lowercase
from copy import deepcopy
import logging # loglevel set by caller
	
def normalize(s):
	return "".join(sorted(s))

def processDictionary(dictPath):
	dictFile = open(dictPath, "r")
	d={}
	for c in ascii_lowercase:
		d[c]=[]
	for dictLine in dictFile:
		line=dictLine.strip()
		d[line[0]].append({
			'lastChar':line[-1],
			'middle':normalize(line[1:-1]), 
			'original':line, 
			'len':len(line), 
			'used':False
		})
	dictFile.close()
	logging.debug(d)
	return d

def processInput(inputPath, dict):
	inputFile = open(inputPath, "r")
	n=0
	for inputLine in inputFile:
		line=inputLine.strip()
		logging.debug(line)
		s=len(line)
		n=n+1
		match=0
		d=deepcopy(dict)
		for ch in range(0,s):
			for item in d[line[ch]]:
				if ch+item['len']<=s and not item['used']:
					if item['lastChar']==line[ch+item['len']-1] and item['middle']==normalize(line[ch+1:ch+item['len']-1]):
							match=match+1
							item['used']=True
							logging.debug((" "*ch)+item['original'])
		print("Case #"+str(n)+": "+str(match))	
	inputFile.close()

