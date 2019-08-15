
from p007prime import prime_generator

LIMIT = 1000000

if __name__ == "__main__":
	primes = []
	for prime in prime_generator():
		if prime > LIMIT:
			break
		primes.append(prime)
	solutions = []
	max_total = 0
	max_seq_len = 0
	for start in range(len(primes)):
		seq = []
		if primes[start]*max_seq_len > LIMIT:
			break
		for number in primes[start:]:
			if sum(seq)+number < LIMIT:
				seq.append(number)
			else:
				break
			total = sum(seq)
			seq_len = len(seq)
			if total in primes:
				if seq_len > max_seq_len:
					max_seq_len = seq_len
					max_total = total
	print(f'prime: {max_total}, consecutive: {max_seq_len}')
