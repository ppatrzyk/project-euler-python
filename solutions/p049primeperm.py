
from p037truncableprime import is_prime2
from collections import Counter
import itertools

if __name__ == "__main__":
	primes = [n for n in range(1000, 10000, 1) if is_prime2(n)]
	digits = [tuple(sorted([int(el) for el in list(str(number))])) for number in primes]
	digit_permissible = [key for key, val in Counter(digits).items() if val > 3]
	for digits in digit_permissible:
		prime_numbers = []
		for perm in itertools.permutations(digits):
			if perm[0] == 0:
				continue
			number = int(''.join([str(el) for el in perm]))
			if is_prime2(number):
				prime_numbers.append(number)
		if len(prime_numbers) >= 3:
			for seq in itertools.combinations(prime_numbers, 3):
				seq = sorted(seq)
				if seq[1]-seq[0] == seq[2]-seq[1]:
					print(seq)

			