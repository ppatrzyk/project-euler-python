
from p004palindrome import is_palindrome
import itertools

ITER_LIMIT = 50
NUMBER_LIMIT = 10000

def reverse_num(n):
	n = str(n)
	reverse = n[::-1]
	reverse = int(reverse)
	return reverse

if __name__ == "__main__":

	lychrel_count = 0

	for candidate in range(1, NUMBER_LIMIT):
		current_candidate = candidate
		for _ in range(ITER_LIMIT):
			current_candidate += reverse_num(current_candidate)
			if is_palindrome(current_candidate):
				break
		else:
			lychrel_count += 1
	print(lychrel_count)

