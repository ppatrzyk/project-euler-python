from p002evenfibonacci import fibonacci

DIGITS = 1000

if __name__ == "__main__":
	for i, fibonacci in enumerate(fibonacci()):
		length = len(str(fibonacci))
		if length >= DIGITS:
			print(i)
			break
