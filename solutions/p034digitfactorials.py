



from math import factorial
import itertools

if __name__ == "__main__":

	numbers = []
	for digits in range(2, 10):
		for array in itertools.combinations_with_replacement(range(10), digits):
			digit_sum = sum([factorial(n) for n in array])
			sum_digits = tuple(int(el) for el in list(str(digit_sum)))
			if digits == len(sum_digits):
				if sorted(array) == sorted(sum_digits):
					numbers.append(digit_sum)
	result = sum(numbers)
	print(result)
