
NUMBER = 600851475143

def get_prime_factors(n):
	factor_list = []
	current_factor = 2
	while True:
		if not (n % current_factor):
			factor_list.append(current_factor)
			n /= current_factor
			if n == 1:
				break
		else:
			current_factor += 1
	return factor_list

factors = get_prime_factors(NUMBER)
print(max(factors))