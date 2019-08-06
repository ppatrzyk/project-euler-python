
import itertools
import math

LIMIT = 100
max_power = int(math.floor(math.log(LIMIT, 2)))

def factor_power(pair):
	number = pair[0]
	power = pair[1]
	for p in range(max_power, 1, -1):
		root = number**(1/p)
		diff = abs(root-int(root))
		if not diff:
			number = int(root)
			power *= p
			break
	return((number, power))

if __name__ == "__main__":
	items = set()
	for pair in itertools.product(range(2, LIMIT+1, 1), repeat=2):
		factored = factor_power(pair)
		items.add(factored)
	result = len(items)
	print(result)

