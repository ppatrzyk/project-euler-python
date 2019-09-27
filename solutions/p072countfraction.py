
import sys
import math
import itertools
import random
from multiprocessing import Pool
from p069totientmax import totient

LIMIT = 10**6

if __name__ == "__main__":
	denominators = list(range(2, LIMIT+1))
	denominators = random.sample(denominators, len(denominators))
	with Pool(processes=8) as pool:
		fractions = pool.map(totient, denominators)
	result = sum(fractions)
	print(result)
