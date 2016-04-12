'''
Creates .tsv file from Yelp Academic Dataset to match desired output.
Usage: python2 si618_hw2_jpgard.py yelp_academic_dataset.json si618_hw2_jpgard_output.tsv
'''

import json, sys
from collections import defaultdict

def make_data(filename):

	raw = open(filename, 'r')
	# output = defaultdict(dict)
	output = []
	for line in raw:
		x = json.loads(line)
		if x['type'] == "business":
			name = x['name'].encode('utf-8')
			city = x.get('city', 'NA').encode('utf-8')
			state = x.get('state', 'NA').encode('utf-8')
			stars = str(x.get('stars', 'NA')).encode('utf-8')
			review_count = str(x.get('review_count', 'NA')).encode('utf-8')
			try: main_category = x.get('categories', ['NA'])[0].encode('utf-8')
			except IndexError: main_category = 'NA'.encode('utf-8')
			#create tuple of (name, city, state, stars, review_count, main_category) and append to output
			output.append((name, city, state, stars, review_count, main_category))

	return output

def write_data(data, destfile):

	outfile = open(destfile, 'w')
	headers = ['name', 'city', 'state', 'stars', 'review_count', 'main_category']
	outfile.write(' \t'.join(headers) + '\n')
	for item in data:
		outfile.write(' \t'.join(item) + '\n')
	outfile.close()

def main():
	filename = sys.argv[1]
	destfile = sys.argv[2]
	data = make_data(filename)
	import ipdb; ipdb.set_trace()
	write_data(data, destfile)

if __name__ == '__main__':
	main()

