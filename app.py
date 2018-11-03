import json
import re
import math
import numpy

with open('reviews.json') as json_file:  
    reviews = json.load(json_file)

def cosine(v1, v2):
        return float(numpy.dot(v1,v2) / (numpy.linalg.norm(v1) * numpy.linalg.norm(v2)))	

def removeDups(duplicate): #removes duplicates in an array, used to get unique words
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
	
def docFreq(dictionary,review,dictionaryTotal):
    review = review.split() #get the TF vector for each review
    wordfreq = [0] * dictionaryTotal
    for revWord in review:
        found = revWord in dictionary
        if(found): #throws an error if it's not in the list so this is the workarround
            wordfreq[dictionary.index(revWord)]+=1
    return wordfreq
	
def main(query,printText):
	allReviews = ""
	reviewTitles = []
	realReview = []
	reviewTokens = dict()
	i=0;
	for i in range(len(reviews)):
		temp = reviews[i]['text'].lower()
		temp = re.sub(r'[^\w\s]','',temp)
		temp = re.sub(r'\b\w{1,2}\b', '', temp)
		rev = " ".join(temp.split())
		reviewTitles.append(reviews[i]['review_id'])
		realReview.append(reviews[i]['text'])
		allReviews += temp + " "
		reviewTokens[i] = temp
		i+=1
	Dictionary = allReviews.split()
	Dictionary = removeDups(Dictionary)
	dictionaryTotal = 0
	for dicWord in Dictionary:
		dictionaryTotal+=1
	wordfreq = [0] * dictionaryTotal
	queryWordFreq = docFreq(Dictionary,query,dictionaryTotal)
	df_t = [0] * dictionaryTotal #initializes variables and gets the TF array for the query
	i=0
	allWordFreq = []
	for line in reviews: #gets the TF array for each review
		wordFreq = docFreq(Dictionary,reviewTokens[i],dictionaryTotal)
		allWordFreq.append(wordFreq)
		j=0
		for freq in wordFreq: #gets the word freq from each documment
			if freq > 0:
				df_t[j] += 1
			j+=1
		i+=1
	IDF = [0] * dictionaryTotal
	i=0
	for df in df_t: #TFIDF found for the query
		IDF[i] = math.log(len(reviews)/df_t[i])
		queryWordFreq[i] = queryWordFreq[i] * IDF[i]#do i need them both j? look 5 lines down double array?
	i+=1
	i=0
	TFIDF = []
	for line in reviews:
		wordFreq = allWordFreq[i]
		j=0
		for df in df_t: #TFIDF found for each reivew
			IDF[j] = math.log(len(reviews)/df_t[j])
			wordFreq[j] = wordFreq[j] * IDF[j]
			j+=1
		TFIDF.append(cosine(queryWordFreq,wordFreq)) #cosine the query TFIDF and each review TFIDF
		i += 1
	#print(IDF)
	zipped = zip(TFIDF,reviewTitles,realReview) #zip and sort the reviews and the weighted TFIDF
	zipped = sorted(zipped, reverse=True) 
	i=0
	print("Rank DocumentID Score") #print the output
	for weight, id, text in zipped:
		if i > 9:
			return
		if printText:
			print(i+1,id,weight,text)
		else:
			print(i+1,id,weight)
		i+=1
		
main("Looking for good burgers",False)