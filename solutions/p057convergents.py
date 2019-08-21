
from fractions import Fraction

ITERS = 1000

if __name__ == "__main__":
	longer_numerator = 0
	current_frac = Fraction(1, 2)
	for _ in range(ITERS):
		result_frac = current_frac + 1
		if len(str(result_frac.numerator)) > len(str(result_frac.denominator)):
			longer_numerator += 1
		current_frac = Fraction(1, 2+current_frac)
	print(longer_numerator)
