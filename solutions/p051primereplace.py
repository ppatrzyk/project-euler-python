
import itertools
from p007prime import prime_generator
from p037truncableprime import is_prime2

if __name__ == "__main__":
	for prime in prime_generator():
		digits = tuple(int(el) for el in list(str(prime)))
		for digits_to_replace in range(1, len(digits)):
			for indices_to_swap in itertools.combinations(range(len(digits)), digits_to_replace):
				test_the_same = set()
				for index in indices_to_swap:
					test_the_same.add(digits[index])
				if len(test_the_same) != 1:
					continue
				primes_all = [prime]
				for number in range(10):
					if (number == 0) and (0 in indices_to_swap):
						continue
					new_digits = list(digits)
					for index in indices_to_swap:
						new_digits[index] = number
					new_number = int(''.join([str(el) for el in new_digits]))
					if is_prime2(new_number):
						primes_all.append(new_number)
				primes_all = set(primes_all)
				if len(primes_all) == 8:
					# print(f'indices {indices_to_swap} primes {primes_all}')
					result = min(primes_all)
					print(result)
					assert False

