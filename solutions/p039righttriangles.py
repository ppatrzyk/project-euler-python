
from math import floor

def get_triplets(p):
	triplets = []
	c_max = int(round((p/2)-1, 0))
	c_possible = range(c_max, 0, -1)
	for c in c_possible:
		c2 = c**2
		a_b = p-c
		a_possible = range(a_b-1, floor(a_b/2), -1)
		for a in a_possible:
			b = a_b-a
			if (a**2 + b**2 == c2):
				triplets.append((a, b, c))
	return triplets

if __name__ == "__main__":
	max_len = 0
	winner_p = None
	for p in range(1, 1001):
		# print(f'runnig {p}')
		triplets = get_triplets(p)
		length = len(triplets)
		if length > max_len:
			max_len = length
			winner_p = p
	print(winner_p)

