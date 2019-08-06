
LAST_RING_LEN = 1001
levels = int((LAST_RING_LEN*2 + (LAST_RING_LEN-2)*2) / 8)

def get_ring():
	level = 1
	last_number = 1
	while True:
		start = last_number+1
		ring_len = level*8
		ring = list(range(start, start+ring_len, 1))
		last_number = ring[-1]
		step_size = level*2
		corner_ind = [-1-(step_size*i) for i in range(4)]
		corners = [ring[ind] for ind in corner_ind]
		level += 1
		yield sum(corners)

if __name__ == "__main__":
	current_sum = 1
	for i, add in enumerate(get_ring(), start=1):
		current_sum += add
		if i == levels:
			break
	print(current_sum)
