import requests
from p81pathsum2 import search, MOVES

if __name__ == "__main__":
    matrix = requests.get('https://projecteuler.net/project/resources/p082_matrix.txt')
    matrix = [[int(el) for el in lis.split(',')] for lis in matrix.text.split('\n') if lis]
    allowed_moves = tuple(MOVES.get(move) for move in ('left', 'up', 'down'))
    finish_possibilities = [(r, len(matrix[0])-1) for r in range(len(matrix))]
    start_possibilities = [(r, 0) for r in range(len(matrix))]
    min_dist = float('inf')
    for finish in finish_possibilities:
        distances = search(matrix, finish, allowed_moves)
        for start in start_possibilities:
            dist = distances.get(start)
            if dist < min_dist:
                print(f'found {min_dist} from {start} to {finish}')
                min_dist = dist
        print(f'{finish} processed')
    print(f'\n\n\n{min_dist}')
