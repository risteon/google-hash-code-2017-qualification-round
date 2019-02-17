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
    print('run knapSack')

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

    selected_vids = vidsize * 0
    cappa = capacity
    cur_vid = nbr_vids - 1
    while cappa >= 0 and cur_vid >= 0:
        # print('cur val: ', K[cur_vid + 1][cappa])
        # print('cur vidsize: ', vidsize[cur_vid])
        if K[cur_vid + 1][cappa] == K[cur_vid][cappa]:
            cur_vid -= 1
        elif K[cur_vid + 1][cappa] == time_gain[cur_vid] + K[cur_vid][cappa-vidsize[cur_vid]]:
            selected_vids[cur_vid] = 1
            cappa -= vidsize[cur_vid]
            cur_vid -= 1
        else:
            assert False
    # print(cappa)

    print('knapsack problem solved')
    # print(K)
    print('selected vids for cache: ', selected_vids)
    print('estimated time gain: ', K[nbr_vids][capacity])
    return K[nbr_vids][capacity], selected_vids


def solve_for_single_cache(problem, cache_id, current_solution):
    print('solve for single cache %d' % cache_id)
    # current_solution.dump()
    # problem.dump()
    time_gain = problem.videos * 0
    # print(time_gain)
    for request_idxs in zip(*np.where(problem.requests > 0)):
        # print('vid, ep: ', request_idxs)
        nbr_reqs = problem.requests[request_idxs]
        # print('nbr: ', nbr_reqs)
        video = request_idxs[0]
        ep = request_idxs[1]
        if problem.endpoints[ep][cache_id] == -1:
            continue
        cur_latency = problem.latency_datacenter[ep]
        # print('cur latency: ', cur_latency)
        for c in range(problem.cache_count):
            if c == cache_id:
                continue
            if problem.endpoints[ep][c] != -1 and current_solution.state[c][video]:
                cur_latency = min(cur_latency, problem.endpoints[ep][c])
                # print('update cur latency: ', cur_latency)
        time_gain[video] += max(0, (cur_latency - problem.endpoints[ep][cache_id]) * nbr_reqs)
        # print('new time gain:', time_gain)
    # print('time_gain: ', time_gain)
    max_time_gain, selected_vids = knapSack(problem.cache_size, problem.videos, time_gain, len(problem.videos))
    assert max_time_gain >= 0
    current_solution.state[cache_id] = np.array(selected_vids, dtype=np.bool)
    return current_solution
