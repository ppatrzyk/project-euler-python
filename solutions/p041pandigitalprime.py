
from p037truncableprime import is_prime2
import itertools

digit_range = range(9, 0, -1)

if __name__ == "__main__":
	for n in digit_range:
		for array in itertools.permutations(range(n, 0, -1), n):
			number = int(''.join([str(el) for el in array]))
			if is_prime2(number):
				print(number)
				break
		else:
			continue
		break
