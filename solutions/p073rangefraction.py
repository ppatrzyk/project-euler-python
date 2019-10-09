
import sys
import math
from fractions import Fraction

D_LIMIT = 12000
LOWER = Fraction(1, 3)
UPPER = Fraction(1, 2)

if __name__ == "__main__":
	fractions = []
	for numerator in range(1, D_LIMIT):
		for denominator in range(numerator+1, D_LIMIT+1):
			if (math.gcd(denominator, numerator) == 1):
				fractions.append(Fraction(numerator, denominator))
		sys.stdout.write(f'{numerator}\r')
	fractions = [el for el in fractions if (el > LOWER and el < UPPER)]
	result = len(fractions)
	print(result)
