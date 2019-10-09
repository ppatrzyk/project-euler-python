
from math import factorial

LIMIT = 10**6

def digit_factorials(n):
	factorials = [factorial(int(num)) for num in list(str(n))]
	res = sum(factorials)
	return res

if __name__ == "__main__":
	count_60 = 0
	for n in range(10, LIMIT):
		current = n
		non_repeating = 1
		hits = []
		while True:
			current = digit_factorials(current)
			if current in hits:
				break
			hits.append(current)
			non_repeating += 1
		# print(f'{n}: count {non_repeating}')
		if non_repeating == 60:
			count_60 += 1
	print(count_60)
