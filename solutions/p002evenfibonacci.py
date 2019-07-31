
LIMIT = (4 * 10**6)

def fibonacci():
	n_2 = 0
	n_1 = 1
	while True:
		yield n_2
		old_n_2 = n_2
		n_2 = n_1
		n_1 = old_n_2 + n_1

if __name__ == "__main__":
	current_sum = 0
	for fibonacci in fibonacci():
		if fibonacci >= LIMIT:
			break
		if not (fibonacci % 2):
			current_sum += fibonacci

	print(current_sum)