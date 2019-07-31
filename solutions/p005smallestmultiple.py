from collections import Counter
from itertools import count
from p003primefactor import get_prime_factors

MAX_DIVISOR = 20

if __name__ == "__main__":
	number_list = list(range(2, MAX_DIVISOR+1))
	divisor_list = []
	while number_list:
		n = number_list.pop()
		factors = get_prime_factors(n)
		if len(factors) > 1:
			# means popped number is not prime
			factors = Counter(factors)
			for key, val in factors.items():
				for power in range(1, val+1):
					divisor = key**power
					try:
						number_list.remove(divisor)
					except:
						pass
		divisor_list.append(n)

	for number in count(MAX_DIVISOR, MAX_DIVISOR):
		# must be multiple of max divisor
		for divisor in divisor_list:
			if (number % divisor):
				break
		else: # no-break
			print(number)
			break





