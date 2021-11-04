import requests
from p081pathsum2 import search, MOVES

if __name__ == "__main__":
	matrix = requests.get('https://projecteuler.net/project/resources/p083_matrix.txt')
	matrix = [[int(el) for el in lis.split(',')] for lis in matrix.text.split('\n') if lis]
	allowed_moves = tuple(MOVES.get(move) for move in ('left', 'right', 'up', 'down'))
	finish = (len(matrix)-1, len(matrix[0])-1)
	distances = search(matrix, finish, allowed_moves)
	print(f'original dimensions: {(len(matrix), len(matrix[0]))}')
	print(distances.get((0, 0)))
