
import itertools
import math

NUMBERS = list(range(1, 11))
LEN_NUMBERS = int(len(NUMBERS))
MIN_TOTAL = sum(NUMBERS[:3])
MAX_TOTAL = sum(NUMBERS[-3:])

def roll_solution(solutions):
	solutions = tuple(reversed(solutions))
	current_min = None
	current_min_index = None
	for i, entry in enumerate(solutions):
		start = entry[0]
		if (current_min is None) or (current_min > start):
			current_min = start
			current_min_index = i
	new_solutions = solutions[current_min_index:] + solutions[:current_min_index]
	return tuple(new_solutions)


if __name__ == "__main__":
	solutions_all = []
	for comb in itertools.combinations(NUMBERS, LEN_NUMBERS//2):
		remainder = [n for n in NUMBERS if n not in comb]
		for perm in itertools.permutations(comb):
			pairs = [(perm[i-1], perm[i]) for i in range(0, LEN_NUMBERS//2)]
			for exp_total in range(MIN_TOTAL, MAX_TOTAL+1, 1):
				solutions = []
				used_n = []
				for pair in pairs:
					pair_sum = sum(pair)
					for n in remainder:
						if n in used_n:
							continue
						total = pair_sum + n
						if total == exp_total:
							triplet = list(pair)
							triplet.append(n)
							used_n.append(n)
							solutions.append(tuple(reversed(triplet)))
				if len(solutions) == LEN_NUMBERS//2:
					solutions_all.append(roll_solution(solutions))
	solutions_all = list(set(solutions_all))
	max_concat = 0
	for sol in solutions_all:
		number_str = ''.join([''.join([str(n) for n in el]) for el in sol])
		if len(number_str) == 16:
			number = int(number_str)
			if number > max_concat:
				max_concat = number
	print(max_concat)
