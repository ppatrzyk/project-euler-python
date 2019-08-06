from math import factorial
from itertools import permutations

N = 10**6
digits = list(range(10))

if __name__ == "__main__":
	perms = permutations(digits)
	for i, perm in enumerate(perms, start=1):
		if i == N:
			print(perm)
			break
