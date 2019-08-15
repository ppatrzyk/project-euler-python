
from functools import reduce

I_IND = [1, 10, 100, 1000, 10000, 100000, 1000000]

def digit_gen():
	number = 1
	while True:
		digits = [int(el) for el in list(str(number))]
		for digit in digits:
			yield digit
		number += 1

if __name__ == "__main__":
	digits = []
	for i, digit in enumerate(digit_gen(), start=1):
		if i in I_IND:
			digits.append(digit)
			if len(digits) == len(I_IND):
				break
	result = reduce(lambda x, y: x*y, digits, 1)
	print(result)
