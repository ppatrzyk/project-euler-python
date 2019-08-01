from math import ceil, sqrt

def triangle_gen():
	i = 0
	current = 0
	while True:
		i += 1
		current += i
		yield current

def get_divisors(n):
	divisors = []
	for i in range(1, ceil(sqrt(n)+1), 1):
		if not (n % i):
			divisors.append(i)
			complement = int(n/i)
			if i != complement:
				divisors.append(complement)
	return sorted(divisors)

if __name__ == "__main__":
	for num in triangle_gen():
		divisors = get_divisors(num)
		if len(divisors) > 500:
			print(num)
			break
