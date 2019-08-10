
from p007prime import prime_generator
import sys
import math
import itertools

LIMIT = 10**6

def rotations(array):
	array = list(array)
	rotations = list((array[i:] + array[ :i]) for i in range(len(array)))
	for rotation in rotations:
		while True:
			if not rotation[0]:
				rotation.pop(0)
			else:
				break
	rotations = [tuple(el) for el in rotations]
	return rotations

if __name__ == "__main__":
	circular = 0
	primes = []
	for prime in prime_generator():
		if prime > LIMIT:
			break
		primes.append(prime)
	total = len(primes)
	digits = tuple(tuple(int(el) for el in tuple(str(n))) for n in primes)
	found = []
	for i, array in enumerate(digits, start=1):
		for rotation in rotations(array):
			if rotation not in digits:
				break
		else:
			# sys.stdout.write(f'{str(array)}\n')
			found.append(array)
		sys.stdout.write(f'\r{round(i/total, 2)}')
	print('\n--------------\n')
	result = len(found)
	print(result)
