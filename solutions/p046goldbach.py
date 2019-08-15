
from p007prime import prime_generator
from p037truncableprime import is_prime2
import itertools

def twice_squares():
	gen = (2*(n**2) for n in itertools.count(1))
	return gen

def odd_comp_gen():
	n = 1
	while True:
		n += 1
		if (is_prime2(n) or not (n % 2)):
			continue
		yield n

if __name__ == "__main__":
	for number in odd_comp_gen():
		for prime in prime_generator():
			failure = False
			if prime >= number:
				print(number)
				assert False
			for square in twice_squares():
				# print(f'number {number} prime {prime}, square {square}')
				current_sum = prime+square
				if current_sum == number:
					failure = True
					break
				if current_sum > number:
					break
			if failure:
				break
