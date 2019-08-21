
from p044pentagon import pentagonal_gen
from p045trianpenthex import hex_gen

# limit from 1000 to 10000

def triangle_gen():
	n = 0
	while True:
		n += 1
		res = n*(n+1)/2
		yield res

def square_gen():
	n = 0
	while True:
		n += 1
		res = n**2
		yield res

def heptagonal_gen():
	n = 0
	while True:
		n += 1
		res = n*(5*n-3)/2
		yield res

def octagonal_gen():
	n = 0
	while True:
		n += 1
		res = n*(3*n-2)
		yield res

def get_list(generator, start=1000, end=10000):
	res = []
	for n in generator():
		if n >= end:
			break
		if n >= start:
			res.append(int(n))
	return res

def start(n):
	start = int(str(n)[:2])
	return start

def end(n):
	end = int(str(n)[2:])
	return end

if __name__ == "__main__":
	numbers = [
		get_list(triangle_gen),
		get_list(square_gen),
		get_list(pentagonal_gen),
		get_list(hex_gen),
		get_list(heptagonal_gen),
		get_list(octagonal_gen)
	]
	# from problem statement 0 cannot appear on 3rd place
	numbers = [[(start(n), end(n)) for n in li if (str(n)[2] != '0')] for li in numbers]
	states = [((5, el), ) for el in numbers[5]]
	while True:
		state = states.pop()
		indices = [el for el in range(6) if el not in [entry[0] for entry in state]]
		if not indices:
			end_last = state[-1][-1][-1]
			start_first = state[0][-1][0]
			if start_first == end_last:
				result = sum([int(''.join([str(el) for el in entry[-1]])) for entry in state])
				print(result)
				break
		end_n = state[-1][-1][-1]
		for index in indices:
			li = numbers[index]
			candidates = [tup for tup in li if tup[0] == end_n]
			if candidates:
				for candidate in candidates:
					new_state = list(state)
					new_state.append((index, candidate))
					states.append(tuple(new_state))
