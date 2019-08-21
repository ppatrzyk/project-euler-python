
import itertools

MAX_MULT = 6

if __name__ == "__main__":
	for no_digits in itertools.count(2):
		start = 10**(no_digits-1)
		end = int(10**no_digits // MAX_MULT)+1
		for number in range(start, end):
			multiples = tuple(number*m for m in range(1, MAX_MULT+1))
			multiples_digits = tuple(tuple(int(el) for el in list(str(number))) for number in multiples)
			test = set((tuple(sorted(number)) for number in multiples_digits))
			if len(test) == 1:
				result = multiples[0]
				print(result)
				break
		else:
			continue
		break
