
LIMIT = 1000

if __name__ == "__main__":
	multiples_3 = set(range(0, LIMIT, 3))
	multiples_5 = set(range(0, LIMIT, 5))
	multiples_all = set.union(multiples_3, multiples_5)
	result = sum(multiples_all)

	print(result)
