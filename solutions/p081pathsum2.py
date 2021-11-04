import sys
import itertools
import requests

# Dijkstra algorithm

MOVES = {
	'right': (0, 1),
	'left': (0, -1),
	'up': (-1, 0),
	'down': (1, 0)
}

def get_value(matrix, coords):
	"""
	Get value from original matrix
	"""
	r = coords[0]
	c = coords[1]
	val = matrix[r][c]
	return val

def initialize_problem(matrix, finish):
	"""
	Init problem
	"""
	nrow = len(matrix)
	ncol = len(matrix[0])
	nodes = list(itertools.product(range(nrow), range(ncol)))
	distances = {node: float('inf') for node in nodes}
	distances[finish] = get_value(matrix, finish)
	return distances

def get_neighbors(current_index, moves, matrix):
	"""
	Based on current index generate valid moves
	"""
	nrow = len(matrix)
	ncol = len(matrix[0])
	neighbors = []
	for move in moves:
		new_pos = (
			current_index[0]+move[0],
			current_index[1]+move[1]
		)
		if (new_pos[0] < 0 or
			new_pos[0] >= nrow or
			new_pos[1] < 0 or
			new_pos[1] >= ncol):
			continue
		neighbors.append(new_pos)
	return neighbors

def update_distance(distances, matrix, node_from, node_to):
	"""
	update distance to given node
	"""
	dist_to_node = get_value(matrix, node_to)
	current_value = distances.get(node_to)
	partial_trip = distances.get(node_from)
	new_route = partial_trip + dist_to_node
	if new_route < current_value:
		distances[node_to] = new_route

def search(matrix, finish, allowed_moves):
	"""
	Entrypoint for search
	"""
	processed = 0
	distances = initialize_problem(matrix, finish)
	unvisited = set([finish, ])
	visited = []
	while True:
		processed += 1
		current_min = float('inf')
		current_node = None
		for node in unvisited:
			partial_trip = distances.get(node)
			if partial_trip < current_min:
				current_min = partial_trip
				current_node = node
		try:
			assert current_node is not None
		except Exception as e:
			sys.stdout.write('Search finished\n')
			sys.stdout.write(f'# visited: {len(visited)}\n')
			break
		else:
			unvisited.remove(current_node)
			visited.append(current_node)
			neighbors = get_neighbors(current_node, allowed_moves, matrix)
			unvisited = unvisited.union(neighbors).difference(visited)
			for neighbor in neighbors:
				update_distance(distances, matrix, current_node, neighbor)
	return distances


if __name__ == "__main__":
	matrix = requests.get('https://projecteuler.net/project/resources/p081_matrix.txt')
	matrix = [[int(el) for el in lis.split(',')] for lis in matrix.text.split('\n') if lis]
	allowed_moves = tuple(MOVES.get(move) for move in ('left', 'up'))
	finish = (len(matrix)-1, len(matrix[0])-1)
	distances = search(matrix, finish, allowed_moves)
	print(f'original dimensions: {(len(matrix), len(matrix[0]))}')
	print(distances.get((0, 0)))
