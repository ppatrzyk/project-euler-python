
import math
import mpmath
import itertools
from multiprocessing import Pool
from p003primefactor import get_prime_factors
from p007prime import prime_generator
from p069totientmax import totient

LIMIT = 10**7

ey = math.exp(float(mpmath.euler))

def min_tot(n):
	loglog = math.log(math.log(n))
	res = n / (ey * loglog + (3 / loglog))
	return math.floor(res)

def sort_digits(n):
	return sorted(tuple(int(el) for el in list(str(n))))

def is_permutation(a, b):
	return (sort_digits(a) == sort_digits(b))

def check_number(n):
	tot = totient(n)
	if not is_permutation(n, tot):
		return False
	else:
		return {'n': n, 'ratio': n/tot}

if __name__ == "__main__":
	# solution cannot be prime since prime-totient cant be permutation
	# -> composite of two primes (the same or similar -- maximizing totient)
	center = LIMIT**0.5
	lim_lower = int(center-1000)
	lim_upper = int(center+1000)
	primes = []
	for prime in prime_generator():
		if prime > lim_lower:
			primes.append(prime)
		if prime > lim_upper:
			break
	solutions = []
	for pair in itertools.combinations_with_replacement(primes, 2):
		n = pair[0]*pair[1]
		if n > LIMIT:
			continue
		solution = check_number(n)
		solutions.append(solution)
	solutions = sorted([el for el in solutions if el], key=lambda el: el['ratio'])
	result = solutions[0]['n']
	print(result)
