
from p004palindrome import is_palindrome

if __name__ == "__main__":
	current_sum = 0
	palindromes_b10 = [n for n in range(1, 10**6, 1) if is_palindrome(n) and int(str(n)[-1])]
	for number in palindromes_b10:
		number_b2 = "{0:b}".format(number)
		if is_palindrome(number_b2):
			current_sum += number
	print(current_sum)
