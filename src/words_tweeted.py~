#!bin/user/python
##Joy Sree Ganesha...Joy Sree Krishna ..Joy Baba Loknath##
'''
Module to count the number of occurances of a single word
'''
def word_count(file):
	lenstr=0
	for word in file.read().split():
		if word not in word_count.wordcount:
			word_count.wordcount[word]=1
			lenstr=len(word)
			if (word_count.maxlen<lenstr):
				word_count.maxlen=lenstr
		else:
			word_count.wordcount[word] =word_count.wordcount[word]+ 1
			lenstr=len(word)
			if (word_count.maxlen<lenstr):
				word_count.maxlen=lenstr
	print_result()
	return 

'''
Module to print the words with their corresponding count
'''
def print_result():
	for k,v in sorted(word_count.wordcount.items()): 
			print k,
			print_result.space=word_count.maxlen-len(k)+3
			for i in range(1,print_result.space):
				print "",
			print v
	return


'''
Initialize variables.
'''	
word_count.wordcount={}
word_count.maxlen=0
print_result.space=0
	
'''
Calling Modules to execute the program
'''
try:	
	file =open("tweet_input/tweets.txt","r+")
	word_count(file)	
	print_result()
	file.close()
except:	
	print "File did not found"

