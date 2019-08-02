from math import factorial

NUMBER = 100

if __name__ == "__main__":
	total = factorial(100)
	digits = [int(el) for el in list(str(total))]
	result = sum(digits)
	print(result)