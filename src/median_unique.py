#!bin/user/python
##Joy Sree Ganesha..Jay Sree Krishna..Jay Baba Loknath###
'''
Module to calculate the median of unique words per tweet. Then I print the Result.
'''
import sys
def med(file):
	for twt in file.read().splitlines():
		med.n=med.n+1		
		for twtword in twt.split():
			if twtword not in med.twtcount:
				med.twtcount[twtword]=1
				med.count=med.count+1
			else:
				med.twtcount[twtword]+=1
						
		if(twt!=''):	
			med.median=med.count+med.median	
			print("%.2f" % (med.median/float(med.n)))	
		med.count=0
		med.twtcount={}
	return

med.twtcount={}
med.count=0
med.median=0
med.n=0
try:
	file =open("tweet_input/tweets.txt","r+")
	med(file)	
	file.close()
except:
	print "The file is not opened"
