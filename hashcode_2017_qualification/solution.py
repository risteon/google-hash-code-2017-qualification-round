# -*- coding: utf-8 -*-

"""Solution module."""

import numpy as np

from .read_input import ProblemInfo


def solve_utility(problem: ProblemInfo):
    assert problem.cache_count == problem.endpoints.shape[-1]

    # calc utility scores per cache per video [ caches x videos ]
    # -> summarize latency gains for all cache-to-endpoint connections

    scores = np.empty(shape=[problem.cache_count, len(problem.videos)], dtype=np.int32)

    # problem.endpoints
    gains = problem.endpoints
    gains[gains == -1] = 0
    gains = problem.endpoints * -1

    cache_gains = np.sum(gains, axis=-1)
    assert cache_gains.shape[0] == problem.cache_count

    video_scores = np.datetime_as_string()

    return None
