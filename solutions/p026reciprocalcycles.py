
def long_div(n, divisor):
	n = [int(el) for el in list(str(n))]
	new_number = []
	afterdot = []
	states = []
	cycle_len = 0
	carry_over = 0
	for digit in n:
		number, remainder = divmod(digit+carry_over, divisor)
		carry_over = remainder*10
		new_number.append(number)
	if carry_over:
		while True:
			number, remainder = divmod(carry_over, divisor)
			state = (number, remainder)
			afterdot.append(number)
			if not remainder:
				break
			if state in states:
				# repeating decimal
				start_ind = states.index(state)
				cycle_len = len(states)-start_ind
				break
			states.append(state)
			carry_over = remainder*10	
	return (new_number, afterdot, states, cycle_len)


if __name__ == "__main__":
	max_cycle = (-1, 0)
	for i in range(1, 1000, 1):
		divide = long_div(1, i)
		cycle_len = divide[3]
		if cycle_len > max_cycle[1]:
			max_cycle = (i, cycle_len)
	result = max_cycle[0]
	print(result)
