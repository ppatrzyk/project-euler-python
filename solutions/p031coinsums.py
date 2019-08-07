
import itertools

GOAL = 200
COINS = (1, 2, 5, 10, 20, 50, 100, 200)

if __name__ == "__main__":
	sums = [1]
	sums.extend(itertools.repeat(0, GOAL))
	for coin in COINS:
		for i in range(GOAL-coin+1):
			sums[i+coin] += sums[i]
	result = sums[-1]
	print(result)
