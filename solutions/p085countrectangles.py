import itertools
from math import ceil, floor, sqrt

COL_MAX = 2000

def count_grid(r, c):
    """
    Count rectangles for given rows and cols
    """
    possibilities = 0
    for rows, cols in itertools.product(range(1, r+1), range(1, c+1)):
        free_r = (r - rows + 1)
        free_c = (c - cols + 1)
        possibilities += (free_r * free_c)
    return possibilities

def get_middle(min_v, max_v):
    return floor((min_v+max_v)/2)

def bisect_search(r, target=2000000):
    """
    search combination closest to 2 million
    """
    best_score = float('inf')
    previous_score = float('inf')
    c_min = r
    c_max = COL_MAX
    best_pair = (r, c_max)
    while True:
        current_c = get_middle(c_min, c_max)
        possibilities = count_grid(r, current_c)
        score = abs(target - possibilities)
        if score >= previous_score:
            # print(f'checking rows={r}, best_score: {best_score}', end='\r')
            break
        previous_score = score
        if score < best_score:
            best_score = score
            best_pair = (r, current_c)
        if possibilities < target:
            c_min = current_c
        elif possibilities > target:
            c_max = current_c
    return((best_pair, score))


if __name__ == "__main__":
    results = list(map(bisect_search, range(2, ceil(sqrt(COL_MAX)+1))))
    results.sort(key=lambda el: el[1])
    best_tuple = results[0][0]
    print('\n\n')
    print(best_tuple[0]*best_tuple[1])
