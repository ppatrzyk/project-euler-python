
from math import sqrt, floor
from fractions import Fraction

LIMIT = 10000

def init_frac(i, floor_sqrt_i):
	frac = {
		'a': floor_sqrt_i,
		'numerator': 1,
		'sqrt_part': i,
		'num_part': (-floor_sqrt_i)
	}
	return frac

def mutate_frac(frac):
	numerator_multiplicator = frac.get('numerator')
	numerator_sqrt = frac.get('sqrt_part')
	numerator_num = (-frac.get('num_part'))
	denominator = (numerator_sqrt - numerator_num**2) / numerator_multiplicator
	denominator = int(denominator)
	a = 0
	num_part = numerator_num
	while True:
		a += 1
		num_part -= denominator
		frac_eval = ((sqrt(numerator_sqrt) + num_part) / denominator)
		# print(frac_eval)
		if frac_eval < 1:
			break
	new_frac = {
		'a': a,
		'numerator': denominator,
		'sqrt_part': numerator_sqrt,
		'num_part': num_part
	}
	return new_frac

if __name__ == "__main__":
	odd_periods = 0
	for i in range(1, LIMIT+1, 1):
		sqrt_i = sqrt(i)
		floor_sqrt_i = floor(sqrt_i)
		if not (floor_sqrt_i - sqrt_i):
			continue
		frac = init_frac(i, floor_sqrt_i)
		# first a is whole number, dont track
		states = []
		while True:
			frac = mutate_frac(frac)
			if frac not in states:
				states.append(frac)
			else:
				break
		period_len = len(states)
		if (period_len % 2):
			odd_periods += 1
	print(odd_periods)
