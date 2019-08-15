
import requests
import string
import re

def is_triangle(result):
	"""
	tn = 1/2n(n+1)
	1/2n^2 + 1/2n - result = 0
	n = -1/2 +- sqrt(0.25+2*result)
	"""
	sqrt_part = (0.25+2*result)**0.5
	n = (-0.5-sqrt_part, -0.5+sqrt_part)
	n_bigger = max(n)
	result = not (n_bigger-int(n_bigger))
	return result

words_url = 'https://projecteuler.net/project/resources/p042_words.txt'

if __name__ == "__main__":
	triangle_words = 0
	raw_names = requests.get(words_url)
	names = [re.sub('\"', '', name.lower()) for name in raw_names.text.split(',')]
	names = sorted(names)
	for name in names:
		name = list(name)
		letters = 0
		for letter in name:
			letter_val = string.ascii_lowercase.index(letter)+1
			letters += letter_val
		if is_triangle(letters):
			triangle_words += 1
	print(triangle_words)

