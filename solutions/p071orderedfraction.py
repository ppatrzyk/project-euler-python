
from fractions import Fraction

LIMIT = 10**6

# target 3/7
if __name__ == "__main__":
	mult = LIMIT // 7
	frac = Fraction((3*mult)-1, 7*mult)
	print(frac.numerator)
	