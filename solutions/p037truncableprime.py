
import sys
from p007prime import prime_generator, is_prime

STOP = 11

def is_prime2(number):
	if number == 1:
		return False
	elif number == 2:
		return True
	else:
		return is_prime(number)


def check_left(digits):
	number_length = len(digits)
	for r in range(number_length):
		truncated = digits[r:]
		truncated = int(''.join([str(el) for el in truncated]))
		if not is_prime2(truncated):
			return False
	return True

def check_right(digits):
	number_length = len(digits)
	for r in range(1, number_length+1):
		truncated = digits[:r]
		truncated = int(''.join([str(el) for el in truncated]))
		if not is_prime2(truncated):
			return False
	return True

if __name__ == "__main__":

	found = []
	for i, number in enumerate(prime_generator(), start=1):
		if number in [2, 3, 5, 7]:
			continue
		if len(found) == STOP:
			break
		digits = tuple(int(el) for el in tuple(str(number)))
		if (not check_left(digits)) or (not check_right(digits)):
			continue
		# sys.stdout.write(f'found: {number}\n')
		found.append(number)	

	result = sum(found)
	print(result)
