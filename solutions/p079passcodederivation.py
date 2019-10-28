
import sys
import requests
import itertools

def check_validity(passcode, partial):
	indices = []
	for el in partial:
		for i, pass_el in enumerate(passcode):
			if el == pass_el:
				indices.append(i)
				break
	if len(indices) < len(partial):
		return False
	else:
		if indices == sorted(indices):
			return True
		else:
			return False


if __name__ == "__main__":
	raw_passcodes = requests.get('https://projecteuler.net/project/resources/p079_keylog.txt')
	passcodes = [list(passcode) for passcode in raw_passcodes.text.split('\n')]
	passcodes = [[int(n) for n in el] for el in passcodes if el]
	unique_numbers = set(itertools.chain(*passcodes))
	for perm in itertools.permutations(unique_numbers):
		for partial in passcodes:
			check = check_validity(perm, partial)
			if not check:
				break
		else:
			sys.stdout.write(f'found: {perm}')
			break
