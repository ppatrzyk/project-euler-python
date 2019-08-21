
LIMIT = 99

if __name__ == "__main__":
	max_sum = 0
	for n in range(LIMIT, 1, -1):
		for power in range(LIMIT, LIMIT-10, -1):
			number = n**power
			digit_sum = sum([int(el) for el in list(str(number))])
			if digit_sum > max_sum:
				max_sum = digit_sum
	print(max_sum)
