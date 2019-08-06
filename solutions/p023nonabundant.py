from p012divisibletrian import get_divisors
import itertools

LIMIT = 28123

def is_abundant(n):
	divisors = set([el for el in get_divisors(n) if el != n])
	result = sum(divisors) > n
	return result

if __name__ == "__main__":
	numbers = list(range(1, LIMIT+1, 1))
	abundant_numbers = [n for n in numbers if is_abundant(n)]
	pairs = [sum(pair) for pair in itertools.combinations(abundant_numbers, 2)]
	pairs.extend([n*2 for n in abundant_numbers])
	sums = set(pairs)
	cannot_be_written_sum = 0
	for n in numbers:
		if n not in sums:
			cannot_be_written_sum += n
	print(cannot_be_written_sum)
