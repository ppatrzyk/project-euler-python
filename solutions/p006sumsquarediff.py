
MAX_NUMBER = 100

if __name__ == "__main__":
	numbers = list(range(1, MAX_NUMBER+1))
	sum_squares = sum([el**2 for el in numbers])
	square_sum = sum(numbers)**2
	result = square_sum - sum_squares

	print(result)