
POWER = 10**3

if __name__ == '__main__':
	total = 2**POWER
	digits = [int(el) for el in list(str(total))]
	result = sum(digits)
	print(result)