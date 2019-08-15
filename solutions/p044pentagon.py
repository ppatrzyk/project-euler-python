
import itertools

diff_limit = 10**8

def is_pentagonal(result):
	sqrt_part = (0.25 + 6*result)**0.5
	n = (1.0/3*(0.5-sqrt_part), 1.0/3*(0.5+sqrt_part))
	n_bigger = max(n)
	result = not (n_bigger-int(n_bigger))
	return result

def pentagonal_gen():
	n = 0
	while True:
		n += 1
		res = int(0.5*n*(3*n - 1))
		yield res

def diff_gen(start):
	n = start-1
	current_diff = 0
	while True:
		n += 1
		res = int(3*n + 1)
		current_diff += res
		yield current_diff

if __name__ == "__main__":
	for n, pentagonal in enumerate(pentagonal_gen(), start=1):
		for diff in diff_gen(n):
			if diff > diff_limit:
				break
			if is_pentagonal(diff):
				sum_num = pentagonal+diff
				diff_num = abs(pentagonal-diff)
				if is_pentagonal(sum_num) and is_pentagonal(diff_num):
					print(f'found nums ({pentagonal}, {diff}), sum_num {sum_num}, diff_num {diff_num}')
					assert False

