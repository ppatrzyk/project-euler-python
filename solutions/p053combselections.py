
from p015latticepaths import choose
import itertools
import math

N_LIMIT = 100
GREATER_THAN = 10**6

if __name__ == "__main__":
	counter = 0
	for n in range(1, N_LIMIT+1):
		odd = bool(n%2)
		max_r = math.ceil(n/2)
		for r in itertools.count(max_r):
			comb = choose(n, r)
			if comb > GREATER_THAN:
				if (r == max_r) and odd:
					counter += 1
				else:
					counter += 2
			else:
				break
	print(counter)
