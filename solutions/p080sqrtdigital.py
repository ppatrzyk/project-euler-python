
import itertools
from mpmath import *
from fractions import Fraction
import re
from p066diophantine import continuous_frac_gen

mp.dps = 110

def get_decimal(number, length):
	continued = []
	for i, n in enumerate(continuous_frac_gen(number)):
		continued.append(n)
		if i == (length+200):
			break
	while len(continued) > 1:
		b = continued.pop()
		a = continued.pop()
		add = a + Fraction(1, b)
		continued.append(add)
	frac = continued[0]
	dec = mpf(frac.numerator) / mpf(frac.denominator)
	dec = re.sub('\.', '', str(dec))
	dec_numbers = [int(el) for el in list(dec)][:length]
	res = sum(dec_numbers)
	return res

if __name__ == "__main__":
	total = 0
	for n in range(100):
		sqrt_approx = n**0.5
		if sqrt_approx == int(sqrt_approx):
			continue
		add = get_decimal(n, 100)
		total += add
	print(total)
