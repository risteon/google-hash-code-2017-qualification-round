#!/usr/bin/env python3
import numpy as np


class Solution:
    def __init__(self):
        self.cached_videos = dict()  # set of video ids organized by cache id


def parse_solution(file, cache_count, cache_size, video_sizes):
    assert cache_count > 0
    assert cache_size > 0
    assert all(v > 0 for v in video_sizes)
    sol = Solution()
    num_videos = len(video_sizes)
    spec_cluster = set()
    with open(file) as fin:
        firstline = fin.readline().strip().split(' ')
        assert len(firstline) == 1
        used_caches = int(firstline[0])
        assert 0 <= used_caches <= cache_count
        for i in range(used_caches):
            line = fin.readline().strip().split(' ')
            assert 1 <= len(line) <= 1 + num_videos
            # add cache to set, if not already present
            c = int(line[0])
            assert c not in spec_cluster
            spec_cluster.add(c)

            sol.cached_videos[c] = {int(line[i+1]) for i in range(len(line) - 1)}
            assert len(sol.cached_videos[c]) == len(line) - 1
            vid_size = sum(video_sizes[v] for v in sol.cached_videos[c])
            assert vid_size <= cache_size
    return sol


def compute_score(task, solution):
    saved_micros = 0
    total_requests = 0
    for index, nbr in np.ndenumerate(task.requests):
        if nbr == 0:
            continue
        vid = index[0]
        ep = index[1]

        total_requests += nbr
        cache_conns = task.endpoints[ep]
        datacenter_latency = np.ones_like(cache_conns) * task.latency_datacenter[ep]
        datacenter_latency = np.where(np.logical_and(cache_conns >= 0, solution.state[:, vid]),
                                      cache_conns, datacenter_latency)
        saved_micros += (task.latency_datacenter[ep] - np.min(datacenter_latency)) * nbr * 1000
    print('total requests:', total_requests)
    print('saved micros:', saved_micros)
    print('score:', saved_micros / total_requests)
