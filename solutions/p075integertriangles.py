# similar to p009
from math import floor
import sys
from collections import Counter
import numpy as np
from p003primefactor import get_prime_factors

LIMIT = 1500000

# correct but inefficient

def is_sum_squares(n):
	factors = Counter(get_prime_factors(n))
	for key, val in factors.items():
		if key < 4:
			continue
		odd_count = bool(val % 2)
		if not odd_count:
			continue
		form_4k3 = (key % 4 == 3)
		if form_4k3:
			return False
	return True

def list_triangles(l):
	"""
	a + b + c = l
	a + b > c
	a^2 + b^2 = c^2
	"""
	triangles = []
	c_max = l // 2
	c_possible = range(c_max, 0, -1)
	for c in c_possible:
		c2 = c**2
		a_b = l-c
		min_a2_plus_b2 = 2*((a_b/2)**2)
		if c2 < min_a2_plus_b2:
			break
		a_possible = range(a_b-1, floor(a_b/2), -1)
		for a in a_possible:
			b = a_b-a
			if (a**2 + b**2 == c2):
				solution = (a, b, c)
				triangles.append(solution)
				break
	return triangles

# better solution

def generate_triplets(LIMIT):
	"""
	http://mathworld.wolfram.com/PythagoreanTriple.html
	"""
	M = np.array([3, 4, 5])
	UAD = np.array([
		np.matrix([[1, 2, 2], [-2, -1, -2], [2, 2, 3]]),
		np.matrix([[1, 2, 2], [2, 1, 2], [2, 2, 3]]),
		np.matrix([[-1, -2, -2], [2, 1, 2], [2, 2, 3]])
	])
	while True:
		M = [triplet for triplet in M.reshape(-1, 3) if (sum(triplet) <= LIMIT)]
		yield M
		M = np.dot(M, UAD)

if __name__ == "__main__":
	lengths = []
	for i, triplets in enumerate(generate_triplets(LIMIT)):
		no_triplets = len(triplets)
		if not no_triplets:
			break
		else:
			for triplet in triplets:
				length = sum(triplet)
				lengths.append(length)
	for i, length in enumerate(set(lengths)):
		multiples = LIMIT // length
		if multiples > 1:
			additional = [m*length for m in range(2, multiples+1)]
			lengths.extend(additional)
	lengths_count = Counter(lengths)
	lengths_count = [key for key, val in lengths_count.items() if val == 1]
	result = len(lengths_count)
	print('\n\n\n' + str(result))
