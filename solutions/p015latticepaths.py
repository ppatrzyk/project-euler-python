import math

def choose(n, k):
	return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

N = 20

if __name__ == "__main__":
	print(choose(N*2, N))
