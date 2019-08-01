
from math import floor

if __name__ == "__main__":
	# a + b + c = 1000
	# a + b > c
	# a^2 + b^2 = c^2
	c_possible = range(499, 0, -1)

	for c in c_possible:
		c2 = c**2
		a_b = 1000-c
		a_possible = range(a_b-1, floor(a_b/2), -1)
		for a in a_possible:
			b = a_b-a
			if (a**2 + b**2 == c2):
				result = a*b*c
				print(f'a={a}, b={b}, c={c}\nabc={result}')
				break
		else:
			continue
		break
