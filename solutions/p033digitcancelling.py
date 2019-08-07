
from functools import reduce
from p003primefactor import get_prime_factors

number_range = range(11, 100, 1)

if __name__ == "__main__":

	pairs = []
	for numerator in number_range:
		num_digits = [int(el) for el in list(str(numerator))]
		if 0 in num_digits:
			continue
		for denominator in reversed(number_range):
			if numerator >= denominator:
				break
			den_digits = [int(el) for el in list(str(denominator))]
			if 0 in den_digits:
				continue
			intersect = set([digit for digit in num_digits if digit in den_digits])
			if not intersect:
				continue
			intersect = intersect.pop()
			value = numerator/denominator
			num_new = num_digits.copy()
			num_new.remove(intersect)
			den_new = den_digits.copy()
			den_new.remove(intersect)
			value_new = num_new[0]/den_new[0]
			if value == value_new:
				pair = (numerator, denominator)
				pairs.append(pair)

	res_numerator = 1
	res_denominator = 1
	for pair in pairs:
		res_numerator *= pair[0]
		res_denominator *= pair[1]

	intersect = [factor for factor in get_prime_factors(res_numerator) if factor in get_prime_factors(res_denominator)]
	common = reduce(lambda x, y: x*y, intersect, 1)

	result = (int(res_numerator/common), int(res_denominator/common))
	print(result[1])

