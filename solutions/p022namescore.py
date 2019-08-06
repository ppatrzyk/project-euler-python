
import requests
import string
import re

if __name__ == "__main__":
	raw_names = requests.get('https://projecteuler.net/project/resources/p022_names.txt')
	names = [re.sub('\"', '', name.lower()) for name in raw_names.text.split(',')]
	names = sorted(names)

	name_scores = 0
	for i, name in enumerate(names, start=1):
		name = list(name)
		letters = 0
		for letter in name:
			letter_val = string.ascii_lowercase.index(letter)+1
			letters += letter_val
		name_score = i*letters
		name_scores += name_score
	print(name_scores)
