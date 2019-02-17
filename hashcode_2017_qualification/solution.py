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
