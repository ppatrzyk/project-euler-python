
from p003primefactor import get_prime_factors
from p007prime import prime_generator
import sys
import itertools
import functools
from fractions import Fraction

LIMIT = 10**6

def coprime(a, b):
	a_factors = set(get_prime_factors(a))
	b_factors = set(get_prime_factors(b))
	common = a_factors.intersection(b_factors)
	return (not bool(common))

def list_coprimes(n):
	n_factors = set(get_prime_factors(n))
	not_coprimes = []
	for factor in n_factors:
		not_coprimes.extend(range(factor, n, factor))
	coprimes = [n for n in range(1, n) if n not in not_coprimes]
	return coprimes

def totient(n):
	n_factors = set(get_prime_factors(n))
	res = n
	for factor in n_factors:
		res *= (1 - Fraction(1, factor))
	return int(res)

if __name__ == "__main__":
	current_set = set()
	max_ratio = 0
	max_n = 0
	for i, prime in enumerate(prime_generator()):
		current_set.add(prime)
		n = functools.reduce(lambda x, y: x*y, current_set, 1)
		if n > LIMIT:
			break
		tot = totient(n)
		current_ratio = (n / tot)
		if current_ratio > max_ratio:
			max_ratio = current_ratio
			max_n = n
	print(max_n)
