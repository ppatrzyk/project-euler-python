
LIMIT = 1000

if __name__ == "__main__":
	total = 0
	for i in range(1, LIMIT+1):
		total += i**i
	result = str(total)[-10:]
	print(result)
