
import itertools

divisors = {
	1: 2,
	2: 3,
	3: 5,
	4: 7,
	5: 11,
	6: 13,
	7: 17
}

if __name__ == "__main__":
	numbers = []
	for array in itertools.permutations(range(9, -1, -1), 10):
		if array[0] == 0:
			break
		for start_ind, divisor in divisors.items():
			subarray = array[start_ind:(start_ind+3)]
			subnum = int(''.join([str(el) for el in subarray]))
			if (subnum % divisor):
				break
		else:
			number = subnum = int(''.join([str(el) for el in array]))
			numbers.append(number)
	result = sum(numbers)
	print(result)
