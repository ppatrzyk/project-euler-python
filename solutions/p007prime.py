from itertools import count
from math import ceil, sqrt

PRIME_WHICH = 10001

def is_prime(n):
	candidates = [2]
	candidates.extend(range(3, ceil(sqrt(n)+1), 2))
	for divisor in candidates:
		if not (n % divisor):
			return False
	return True

def prime_generator():
	yield 2
	next_prime = 3
	while True:
		yield next_prime
		while True:
			next_prime += 2
			if is_prime(next_prime):
				break

if __name__ == "__main__":
	for i, prime in enumerate(prime_generator(), start = 1):
		if i == PRIME_WHICH:
			print(f'{i}. prime: {prime}')
			break
