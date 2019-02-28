# -*- coding: utf-8 -*-

"""Solution module."""

import numpy as np
import numba
from numba import jit

# from .read_input import ProblemInfo
# from .write_output import SolutionOutput
from .solve_subproblem import solve_problem

input_array = np.asarray([[2, 3, 0, 0, 0], [2, 1, 3, 5, 0], [7, 2, 3, 0, 0]])


def dummy_solution_for_matrix(score_matrix):
    return np.arange(score_matrix.shape[0])


def dummy_concatenate(list_of_sub_ids):
    return np.concatenate(list_of_sub_ids)


def subdivide_and_solve_subproblems(slide_input_array, slide_ids):
    assert slide_input_array.shape[0] == slide_ids.shape[0]

    max_tolerable_size = 100
    current = 0

    list_of_sub_solution_ids = []

    while True:
        sub_slides = slide_input_array[
                     current:min(current+max_tolerable_size, slide_input_array.shape[0])]
        sub_ids = slide_ids[current:min(current+max_tolerable_size, slide_input_array.shape[0])]
        sub_scores = compute_score_for_submatrix_of_photos(sub_slides)
        sub_solution = solve_problem(sub_scores)

        # permute input IDs according to solution
        sub_solution_ids = sub_ids[sub_solution]
        list_of_sub_solution_ids.append(sub_solution_ids)

        current += max_tolerable_size
        print('images processed', current)
        print('size slide input array', slide_input_array.shape[0])
        if current >= slide_input_array.shape[0]:
            break

    # Todo input concatenation solution
    solution_ids = dummy_concatenate(list_of_sub_solution_ids)
    assert solution_ids.shape[0] == slide_input_array.shape[0]
    return solution_ids


def compute_score_for_submatrix_of_photos(input_array):
    n = input_array.shape[0]
    scores = np.zeros(shape=[n, n], dtype=np.int32)

    for a in range(n):
        for b in range(a+1, n):
            n_intersect = np.intersect1d(input_array[a, :], input_array[b, :]).size - 1
            # find first occurence of zero -> number of unique elements
            n_diff_ab = np.nonzero(input_array[a, :])[0][-1] + 1 - n_intersect
            n_diff_ba = np.nonzero(input_array[b, :])[0][-1] + 1 - n_intersect
            scores[a, b] = min(n_intersect, n_diff_ab, n_diff_ba)
    # mirror along diagonal
    return scores.transpose() + scores
