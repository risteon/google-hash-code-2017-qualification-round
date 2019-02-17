#!/usr/bin/env python3


class Solution():
    def __init__(self):
        self.cached_videos = dict()  # set of video ids organized by cache id


def parse_solution(file, C, cache_size, video_sizes):
    assert C > 0
    assert cache_size > 0
    assert all(v > 0 for v in video_sizes)
    sol = Solution()
    V = len(video_sizes)
    spec_cluster = set()
    with open(file) as fin:
        firstline = fin.readline().strip().split(' ')
        assert len(firstline) == 1
        N = int(firstline[0])
        assert 0 <= N <= C
        for i in range(N):
            line = fin.readline().strip().split(' ')
            assert 1 <= len(line) <= 1 + V
            c = int(line[0])
            assert c not in spec_cluster
            spec_cluster.insert(c)
            sol.cached_videos[c] = {int(line[i+1]) for i in range(len(line) - 1)}
            assert len(sol.cached_videos[c]) == len(line) - 1
            vid_size = sum(video_sizes[v] for v in sol.cached_videos[c])
            assert vid_size <= cache_size
    return sol


def compute_score(task, solution):
    saved_micros = 0
    total_requests = 0
    for request in task.requests:
        vid = request[0]
        ep = request[1]
        nbr = request[2]
        total_requests += nbr
        latency_cache = task.asdf[ep]
        cache_conns = task.endpoints[ep]
        for cache_id, conn in enumerate(cache_conns):
            if conn >= 0 and vid in solution.cached_videos[cache_id]:
                latency_cache = min(latency_cache, conn)
        saved_micros = (task.asdf[ep] - latency_cache) * nbr * 1000
    print('total requests:', total_requests)
    print('saved micros:', saved_micros)
    print('score:', saved_micros / total_requests)
