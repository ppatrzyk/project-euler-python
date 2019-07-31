
MAX_VAL = 999

def mutate(diagonal_root, pair, max_val):
	"""
	moves through pair grid from highest product down
	pair is a tuple of coordinates
	"""
	if pair[0] == max_val:
		# move to next diagonal
		if diagonal_root[0] == diagonal_root[1]:
			# go down
			return (diagonal_root[0], diagonal_root[1]-1), (diagonal_root[0], diagonal_root[1]-1)
		else:
			# go left
			return (diagonal_root[0]-1, diagonal_root[1]), (diagonal_root[0]-1, diagonal_root[1])
	else:
		# move along diagonal
		return diagonal_root, (pair[0]+1, pair[1]-1)

def get_pair(max_val):
	diagonal_root = next_pair = (max_val, max_val)
	while True:
		yield next_pair
		diagonal_root, next_pair = mutate(diagonal_root, next_pair, max_val)

def is_palindrome(n):
	n = str(n)
	result = (n == n[::-1])
	return result

if __name__ == "__main__":
	for pair in get_pair(MAX_VAL):
		result = pair[0]*pair[1]
		if is_palindrome(result):
			print(f'{pair[0]}*{pair[1]} = {result}')
			break
