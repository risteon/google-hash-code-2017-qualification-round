# -*- coding: utf-8 -*-

"""Solution module."""

import numpy as np
import numba
from numba import jit

#from .read_input import ProblemInfo
#from .write_output import SolutionOutput

input_array = np.asarray([[2, 3, 0, 0, 0], [2, 1, 3, 5, 0], [7, 2, 3, 0, 0]])


def compute_score_for_submatrix_of_photos(input_array):
    n = input_array.shape[0]
    scores = np.zeros(shape=[n, n], dtype=np.int32)

    for a in range(n):
        for b in range(a+1, n):
            scores[a, b] = min(np.setdiff1d(input_array[a, :], input_array[b, :]).size,
                               np.setdiff1d(input_array[b, :], input_array[a, :]).size,
                               np.intersect1d(input_array[a, :], input_array[b, :]).size - 1)
    # mirror along diagonal
    return scores.transpose() + scores



# def solve_utility(problem: ProblemInfo):
#     assert problem.cache_count == problem.endpoints.shape[-1]
#     assert problem.latency_datacenter.shape[0] == problem.endpoints.shape[0]
#
#     gains = np.expand_dims(problem.latency_datacenter, axis=-1) - problem.endpoints
#     # zero gain if not connected to cache
#     gains[problem.endpoints == -1] = 0
#
#     # calc utility scores per cache per video [ caches x videos ]
#     # -> summarize latency gains for all cache-to-endpoint connections
#
#     cache_gains = np.sum(gains, axis=0)
#     assert cache_gains.shape[0] == problem.cache_count
#
#     video_scores = np.reciprocal(problem.videos.astype(np.float64))
#
#     scores = np.dot(np.expand_dims(video_scores, axis=-1), np.expand_dims(cache_gains, axis=0))
#
#
#
#     return SolutionOutput()


compute_score_for_submatrix_of_photos(input_array)
