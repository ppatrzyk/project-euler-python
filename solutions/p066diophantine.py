
import itertools
from math import sqrt, floor
from fractions import Fraction
from p064oddperiodsquare import init_frac, mutate_frac

D_LIMIT = 1000

# https://en.wikipedia.org/wiki/Pell%27s_equation

def continuous_frac_gen(num):
	floor_sqrt_num = floor(sqrt(num))
	frac = init_frac(num, floor_sqrt_num)
	yield frac.get('a')
	while True:
		frac = mutate_frac(frac)
		yield frac.get('a')

def convergents_sqrt(num):
	n_2 = None
	n_1 = None
	for i, a in enumerate(continuous_frac_gen(num)):
		if i == 0:
			res = Fraction(a, 1)
			yield res
		elif i == 1:
			res = Fraction((a*n_1 + 1), a)
			yield res
		else:
			res = Fraction(a*n_1.numerator + n_2.numerator, a*n_1.denominator + n_2.denominator)
			yield res
		n_2 = n_1
		n_1 = res

def diophantine_solve(d):
	for i, approx in enumerate(convergents_sqrt(d)):
		x = approx.numerator
		y = approx.denominator
		eq_eval = ((x**2) - (d * (y**2)))
		if eq_eval == 1:
			solution = {
				'd': d,
				'x': x,
				'y': y
			}
			return solution

if __name__ == "__main__":
	d_solutions = []
	for d in range(2, D_LIMIT+1, 1):
		d_sqrt = sqrt(d)
		if (int(d_sqrt)-d_sqrt == 0):
			continue
		solution = diophantine_solve(d)
		# print(f'{d} solution: {solution}')
		d_solutions.append(solution)
	d_solutions = sorted(d_solutions, key=lambda k: k['x'])
	result = d_solutions[-1].get('d')
	print(result)
