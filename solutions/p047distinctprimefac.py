
import itertools
from collections import Counter
from p003primefactor import get_prime_factors

CONSECUTIVE = 4

if __name__ == "__main__":
	previous = []
	for number in itertools.count(2):
		if len(previous) == CONSECUTIVE:
			previous.pop(0)
		factors = Counter(get_prime_factors(number))
		previous.append(factors)
		flat = []
		if len(previous) == CONSECUTIVE:
			for entry in previous:
				if len(entry) != CONSECUTIVE:
					break
				for item in entry.items():
					flat.append(item)
			else:
				if len(flat) == len(set(flat)):
					# print(f'current {number}, fatorlist {previous}')
					break
	result = number - (CONSECUTIVE-1)
	print(result)
	