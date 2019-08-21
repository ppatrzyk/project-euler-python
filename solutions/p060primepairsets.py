
import itertools
from p007prime import prime_generator
from p037truncableprime import is_prime2

SET_LEN = 5
SEARCH_LIMIT = 10000
NUMBER_LIMIT = 10000

# limited depth-first search

def check_candidate(current_set, candidate):
	if not current_set:
		return True
	for el in current_set:
		left = int(str(candidate)+str(el))
		right = int(str(el)+str(candidate))
		if not (is_prime2(left) and is_prime2(right)):
			return False
	return True

def prime_set_search(current_set, set_max=0):
	"""
	valid sets of len+1
	"""
	counter = 0
	if not set_max:
		try:
			set_max = max(current_set)
		except:
			set_max = 2
	for number in prime_generator():
		if number <= set_max:
			continue
		if check_candidate(current_set, number):
			yield set.union(current_set, set([number]))
		else:
			counter += 1
			if (counter >= SEARCH_LIMIT) or (number >= NUMBER_LIMIT):
				yield None


if __name__ == "__main__":
	inter_states = [prime_set_search(set())]
	while (len(inter_states) < (SET_LEN+1)):
		current_generator = inter_states[-1]
		next_combination = next(current_generator)
		if next_combination is None:
			inter_states.pop()
		else:
			if len(inter_states) == SET_LEN:
				result = sum(next_combination)
				print(result)
				break
			inter_states.append(prime_set_search(next_combination))
