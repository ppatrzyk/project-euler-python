
import sys
from p076countingsummations import generalized_pentagonal_gen, count_partitions

def count_partitions2():
	"""
	modified version from p076countingsummations
	mod 10**6 to prevent int overflow
	"""
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
		p_n = (p_n % 10**6)
		partitions.append(p_n)
		yield partitions[-1]

if __name__ == "__main__":
	for i, partitions in enumerate(count_partitions2(), start=0):
		sys.stdout.write(f'{i}: {partitions} partitions\r')
		if not (int(partitions) % int(10**6)):
			break
