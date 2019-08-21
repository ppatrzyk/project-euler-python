
from p037truncableprime import is_prime2

PROP_LIMIT = 0.1

def get_ring():
	"""
	modification of p028spiraldiag
	"""
	level = 1
	last_number = 1
	while True:
		start = last_number+1
		ring_len = level*8
		side_len = int((ring_len+4)/4)
		ring = list(range(start, start+ring_len, 1))
		last_number = ring[-1]
		step_size = level*2
		corner_ind = [-1-(step_size*i) for i in range(4)]
		corners = [ring[ind] for ind in corner_ind]
		level += 1
		yield corners, side_len

if __name__ == "__main__":
	all_diag = [1]
	diag_primes = []
	for corners, side_len in get_ring():
		all_diag.extend(corners)
		diag_primes.extend([n for n in corners if is_prime2(n)])
		prop_primes = len(diag_primes) / len(all_diag)
		if prop_primes < PROP_LIMIT:
			print(side_len)
			break
