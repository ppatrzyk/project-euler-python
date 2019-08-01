
def collatz_gen(n):
	while True:
		yield n
		if not (n % 2):
			n = int(n/2)
		else:
			n = int(3*n + 1)

if __name__ == "__main__":
	max_length = (0, 0) # (starting, length)
	eliminate = set()
	for candidate in range(10**6-1, 0, -1):
		if candidate in eliminate:
			continue
		for i, num in enumerate(collatz_gen(candidate), start=1):
			eliminate.add(num)
			if num == 1:
				break
		if i > max_length[1]:
			max_length = (candidate, i)
	print(max_length[0])