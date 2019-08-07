
import itertools
from collections import Counter

def check_pandigital(*args):
	digits = []
	for arg in args:
		digits.extend(arg)
	if 0 in digits:
		return False
	counted = Counter(digits)
	res = (len(counted) == 9)
	return res

if __name__ == "__main__":
	products = set()
	a_range = range(1, 10000, 1)
	for a in a_range:
		a_digits = [int(el) for el in list(str(a))]
		for b in itertools.count(1):
			b_digits = [int(el) for el in list(str(b))]
			prod = a*b
			prod_digits = [int(el) for el in list(str(prod))]
			no_digits = len(a_digits+b_digits+prod_digits)
			if no_digits > 9:
				break
			elif no_digits == 9:
				res = check_pandigital(a_digits, b_digits, prod_digits)
				if res:
					# print(f'{a}*{b}={prod}')
					products.add(prod)
			else:
				continue
	result = sum(products)
	print(result)
