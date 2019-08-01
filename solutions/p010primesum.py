from p007prime import prime_generator

LIMIT = 2 * 10**6

if __name__ == "__main__":
	prime_sum = 0
	for prime in prime_generator():
		if prime >= LIMIT:
			break
		prime_sum += prime
	print(prime_sum)
