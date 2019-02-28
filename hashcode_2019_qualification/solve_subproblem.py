
import numpy as np

N_swap = 3
swap_id = np.arange(N_swap)
n_no_outer_improves = 5
n_no_inner_improves = 20


def get_score(matrix, path):
    score = 0
    for i in range(len(path) - 1):
        score += matrix[path[i], path[i+1]]
    return score


def solve_problem_new(matrix):
    print(np.max(matrix))
    print(matrix[np.where(matrix > 0)])


def solve_problem(matrix):
    print('max matrix element', np.max(matrix))
    assert matrix.shape[0] == matrix.shape[1]
    n = matrix.shape[0]
    best_path = np.arange(n)
    best_score = get_score(matrix, best_path)
    no_outer_improves = 0
    while no_outer_improves < n_no_outer_improves:
        print(best_score)
        path = np.random.permutation(n)
        score = get_score(matrix, path)
        no_inner_improves = 0
        while no_inner_improves < n_no_inner_improves:
            idxs = np.random.choice(n, N_swap, replace=False)
            perm = np.random.permutation(N_swap)
            while np.all(swap_id == perm):
                perm = np.random.permutation(N_swap)
            nodes = path[idxs]
            perm_nodes = nodes[perm]
            new_path = np.array(path)
            new_path[idxs] = perm_nodes
            new_score = get_score(matrix, new_path)
            if new_score > score:
                score = new_score
                path = new_path
                no_inner_improves = 0
            else:
                no_inner_improves += 1
        if score > best_score:
            best_score = score
            best_path = path
            no_outer_improves = 0
        else:
            no_outer_improves += 1

    print('best score', best_score)
    return best_path
