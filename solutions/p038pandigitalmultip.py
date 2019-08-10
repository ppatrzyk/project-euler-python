
from p032pandigital import check_pandigital

# possibilities:
# 4 5
# 3 3 3
# 2 2 2 3

def run_check(k_range, n_range):
	for k in k_range:
		result = ''
		for n in n_range:
			result += (str(k*n))
		if check_pandigital([int(el) for el in list(result)]):
			pandigital.append(int(result))

if __name__ == "__main__":
	pandigital = []
	# 2 2 2 3
	run_check(k_range=range(25, 34), n_range=range(1, 5))
	# 3 3 3
	run_check(k_range=range(100, 334), n_range=range(1, 4))
	# 4 5
	run_check(k_range=range(5000, 10000), n_range=range(1, 3))
	result = max(pandigital)
	print(result)








