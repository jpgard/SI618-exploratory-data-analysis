#Written by Josh Gardner for SI618 W16

'''
Creates .tsv file from Yelp Academic Dataset to match desired output.
Usage: python2 si618w16_hw4_part1_jpgard.py yelp_academic_dataset.json star_sentimentscore.txt
'''

import nltk, json, sys
from collections import defaultdict

def make_data(filename):
	biz_review_scores = defaultdict(dict)
	word_sentiment = {}
	stemmer = nltk.PorterStemmer()
	raw = open(filename, 'r')

	#build sentiment dictionary from sentimentfile
	sentimentfile = open('sentiment_word_list.txt', 'rU')
	for line in sentimentfile:
	  line = line.strip()
	  word, sentiment = line.split(',')
	  sentiment = int(sentiment)
	  word = stemmer.stem(word)
	  word_sentiment[word] = sentiment

	sentimentfile.close()

	for line in raw:
		x = json.loads(line)
		
		if x['type'] == "review":
			id = x['business_id']
			if id not in biz_review_scores.keys():
				biz_review_scores[id] = defaultdict(list)
			stars = x['stars']
			stems = [stemmer.stem(w) for w in nltk.word_tokenize(x.get('text'))]
			stems_scores = [word_sentiment.get(s, 0) for s in stems]
			review_score = sum(stems_scores)
			biz_review_scores[id]['sentiments'].append(review_score) #update 'sentiments' entry for business
			biz_review_scores[id]['stars'].append(stars) #update 'stars' entry for business
			
	return biz_review_scores

def make_output(data, outfile):
	outfile = open(outfile, 'w')
	#TODO: compute avg_star and avg_sentiment for each entry, write to tab-separated file
	for k,v in data.items():
		avg_star = float(sum(v['stars']))/float(len(v['stars']))
		avg_sentiment = float(sum(v['sentiments']))/float(len(v['sentiments']))
		outfile.write(str(avg_star) + '\t' + str(avg_sentiment) + '\n')
	outfile.close()
	
def main():
	filename = sys.argv[1]
	outfile = sys.argv[2]
	print "building data from reviews..."
	data = make_data(filename)
	print "building data complete. Making output..."
	make_output(data, outfile)
	print "Output complete."

if __name__ == '__main__':
	main()