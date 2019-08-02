
from p012divisibletrian import get_divisors
from collections import Counter

LIMIT = 10000

def d(n):
	divisors = set([el for el in get_divisors(n) if el != n])
	sum_divisors = sum(divisors)
	# print(f'{n}: {sum_divisors}, {divisors}')
	return sum_divisors

if __name__ == "__main__":
	candidates = list(range(LIMIT, 0, -1))
	amicable = []
	while candidates:
		candidate = candidates.pop()
		sum_div = d(candidate)
		if sum_div > LIMIT:
			continue
		if (d(sum_div) == candidate) and (candidate != sum_div):
			# print(f'pair: {candidate}, {sum_div}')
			try:
				candidates.remove(sum_div)
				amicable.append(sum_div)
			except:
				pass
			amicable.append(candidate)
	print(sum(amicable))
	