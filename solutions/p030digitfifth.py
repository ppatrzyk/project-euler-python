
import itertools

POWER = 5

if __name__ == "__main__":
	found = []
	digit_max = 1
	max_powered = 9**POWER
	while True:
		number = int(''.join(['9' for _ in range(digit_max)]))
		sum_digits = digit_max*max_powered
		if number >= sum_digits:
			break
		else:
			digit_max += 1
	for number_list in itertools.product(range(10), repeat=digit_max):
		if not sum(number_list[:-1]):
			continue
		powers = [n**POWER for n in number_list]
		sum_digits = sum(powers)
		number = int(''.join([str(el) for el in number_list]))
		if number == sum_digits:
			found.append(number)
	result = sum(found)
	print(result)
