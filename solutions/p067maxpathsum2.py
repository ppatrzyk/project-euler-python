
from p018maxpathsum import prune
import requests

if __name__ == "__main__":
	raw_triangle = requests.get('https://projecteuler.net/project/resources/p067_triangle.txt')
	triangle = [[int(el) for el in lis.split()] for lis in raw_triangle.text.split('\n') if lis]
	while len(triangle) > 1:
		triangle = prune(triangle)
	print(triangle)
