
from p007prime import prime_generator
import sys
import itertools
from copy import copy

DESIRED_SOLUTIONS = 5000

def mutate_state(state, goal, success):
	new_states = []
	try:
		state_max = max(state)
	except:
		state_max = 0
	state_total = sum(state)
	if state_total == goal:
		success.append(state)
	else:
		for prime in primes:
			if prime < state_max:
				continue
			if (state_total + prime) > goal:
				break
			else:
				new_state = copy(state)
				new_state.append(prime)
				new_states.append(new_state)
	return new_states

def search_prime_partitions(n):
	success = []
	states = [[]]
	while states:
		state = states.pop()
		new_states = mutate_state(state, n, success)
		states.extend(new_states)
	return success

if __name__ == "__main__":
	primes = []
	for i, prime in enumerate(prime_generator()):
		primes.append(prime)
		if i == 100000:
			break

	for n in itertools.count(1):
		res = search_prime_partitions(n)
		no_solutions = len(res)
		sys.stdout.write(f'{n}: {no_solutions} solutions\r')
		if no_solutions >= DESIRED_SOLUTIONS:
			break
			