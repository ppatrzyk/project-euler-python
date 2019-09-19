from math import exp, sqrt, floor
from fractions import Fraction

def e_approx(steps):
	a_sequence = [int(2*(i+1) / 3) if (i % 3 == 2) else 1 for i in range(steps)]
	a_sequence[0] = 2
	a_sequence = reversed(a_sequence)
	numerator = 1
	denominator = 0
	for a in a_sequence:
		old_denominator = denominator
		denominator = numerator
		numerator = old_denominator + a*numerator
	return Fraction(numerator, denominator)

if __name__ == "__main__":
	approximation = e_approx(100)
	numerator = approximation.numerator
	result = sum([int(el) for el in list(str(numerator))])
	print(result)