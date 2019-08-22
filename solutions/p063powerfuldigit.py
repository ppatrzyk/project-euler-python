
import itertools

if __name__ == "__main__":
	count = 0
	break_all = False
	for power in itertools.count(1):
		starting_count = count
		for base in itertools.count(1):
			res = int(base**power)
			res_digits = len(str(res))
			if res_digits == power:
				count += 1
			if res_digits > power:
				if count == starting_count:
					break_all = True
				# print(f'breaks at base {base} power {power}, current count {count}')
				break
		if break_all:
			break
	print(count)
