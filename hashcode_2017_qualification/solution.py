# -*- coding: utf-8 -*-

"""Solution module."""

import numpy as np

from .read_input import ProblemInfo
from .write_output import SolutionOutput


def solve_utility(problem: ProblemInfo):
    assert problem.cache_count == problem.endpoints.shape[-1]
    assert problem.latency_datacenter.shape[0] == problem.endpoints.shape[0]

    gains = np.expand_dims(problem.latency_datacenter, axis=-1) - problem.endpoints
    # zero gain if not connected to cache
    gains[problem.endpoints == -1] = 0

    # calc utility scores per cache per video [ caches x videos ]
    # -> summarize latency gains for all cache-to-endpoint connections

    cache_gains = np.sum(gains, axis=0)
    assert cache_gains.shape[0] == problem.cache_count

    video_scores = np.reciprocal(problem.videos.astype(np.float64))

    scores = np.dot(np.expand_dims(video_scores, axis=-1), np.expand_dims(cache_gains, axis=0))



    return SolutionOutput()


# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
def knapSack(capacity, vidsize, time_gain, nbr_vids):
    K = [[0 for x in range(capacity + 1)] for x in range(nbr_vids + 1)]

    # Build table K[][] in bottom up manner
    for i in range(nbr_vids + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif vidsize[i-1] <= w:
                K[i][w] = max(time_gain[i-1] + K[i-1][w-vidsize[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[nbr_vids][capacity]


def solve_for_single_cache(problem, cache_id, current_solution):
    time_gain = vidsize * 0
