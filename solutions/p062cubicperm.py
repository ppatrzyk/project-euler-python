
import itertools

def which(li, find):
	for i, el in enumerate(li):
		if el == find:
			return i
	return None

if __name__ == "__main__":
	digit_tuples = []
	counts = []
	numbers = []
	for number in itertools.count(1):
		cube = number**3
		cube_digits = tuple(sorted(list(str(cube))))
		index = which(digit_tuples, cube_digits)
		if index is None:
			digit_tuples.append(cube_digits)
			counts.append(1)
			numbers.append([cube])
		else:
			counts[index] += 1
			numbers[index].append(cube)
			if counts[index] == 5:
				result = numbers[index][0]
				print(result)
				break
