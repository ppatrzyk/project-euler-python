
# https://en.wikipedia.org/wiki/Pentagonal_number_theorem

LIMIT = 100

def generalized_pentagonal_gen():
	"""
	p044 modification
	"""
	n = 0
	while True:
		res = int(0.5*n*(3*n - 1))
		yield (n, res)
		if n == 0:
			n += 1
		elif n < 0:
			n = -n
			n += 1
		else:
			n = -n

def count_partitions():
	partitions = [1, 1] # p(0)=0
	yield partitions[-2]
	yield partitions[-1]
	n = 2
	while True:
		p_n = 0
		for i, pentagonal in enumerate(generalized_pentagonal_gen(), start=1):
			k = pentagonal[0]
			g_k = pentagonal[1]
			if k == 0:
				continue
			partitions_index = n-g_k
			# print(f'{n}: {partitions_index}')
			if partitions_index < 0:
				break
			add_term = ((-1)**(k-1))*partitions[partitions_index]
			p_n += add_term
		n += 1
		partitions.append(p_n)
		yield partitions[-1]


if __name__ == "__main__":
	for i, partitions in enumerate(count_partitions(), start=0):
		# print(f'result: {i}: {partitions}')
		if i == LIMIT:
			break
	result = partitions-1
	print(result)
