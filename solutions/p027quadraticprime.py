
from p007prime import is_prime
import itertools

LIMIT = 1000

def get_poly(a, b):
	def f(n):
		res = n**2 + a*n + b
		return res
	return f

def get_consec_primes(a, b):
	f = get_poly(a, b)
	n = 0
	while True:
		res = abs(f(n))
		if not is_prime(res):
			break
		else:
			n += 1
	return n


if __name__ == "__main__":
	a = range(-LIMIT+1, LIMIT, 1)
	b = range(-LIMIT, LIMIT+1, 1)

	current_max = (False, False, 0) # a, b, length
	for a, b in itertools.product(a, b):
		primes_len = get_consec_primes(a, b)
		if primes_len > current_max[2]:
			current_max = (a, b, primes_len)
	max_a = current_max[0]
	max_b = current_max[1]
	result = max_a*max_b
	print(result)