import numpy as np

class ProblemInfo:
    def __init__(self):
        self.videos = None  # list of video sizes
        self.cache_size = None  # integer
        self.cache_count = None  # integer
        self.latency_datacenter = None  # numpy array of length number of endpoints
        self.endpoints = None  # numpy array of num_endpoints x num_cache; if connection, list latency, otherwise -1 (int32)
        self.requests = None  # list of list with 3 entries [video, endpoint, requests]

"""EXAMPLE
5 2 4 3 100
50 50 80 30 110
1000 3
0 100
2 200
1 300
500 0
3 0 1500
0 1 1000
4 0 500
1 0 1000
5 videos, 2 endpoints, 4 request descriptions, 3 caches 100MB each.
Videos 0, 1, 2, 3, 4 have sizes 50MB, 50MB, 80MB, 30MB, 110MB.
Endpoint 0 has 1000ms datacenter latency and is connected to 3 caches:
The latency (of endpoint 0) to cache 0 is 100ms.
The latency (of endpoint 0) to cache 2 is 200ms.
The latency (of endpoint 0) to cache 1 is 300ms.
Endpoint 1 has 500ms datacenter latency and is not connected to a cache.
1500 requests for video 3 coming from endpoint 0.
1000 requests for video 0 coming from endpoint 1.
500 requests for video 4 coming from endpoint 0.
1000 requests for video 1 coming from endpoint 0.
"""


def split_first_line(line):
    info = line.split(' ')  # num_videos, num_endpoints, num_requests, num_caches, cache_size
    assert len(info) == 5
    return int(info[0]), int(info[1]), int(info[2]), int(info[3]), int(info[4])


def parse_input(filename):
    file = open(filename)

    problem_obj = ProblemInfo()
    num_videos = 0
    num_endpoints = 0
    num_requests = 0
    num_caches = 0
    cache_size = 0

    for idx, line in enumerate(file):
        # read first line
        if idx == 0:
            num_videos, num_endpoints, num_requests, num_caches, cache_size = split_first_line(line)
            print('first line')
            print(split_first_line(line))
        # read video sizes
        if idx == 1:
            video_sizes = line.split(' ')
            print(len(video_sizes), num_videos)
            assert len(video_sizes) == num_videos
            problem_obj.videos = np.array(video_sizes, dtype=np.int32)
            print('video sizes')
            print(problem_obj.videos)




    return None


parse_input('/lhome/ltriess/documents/Google_Hash_Code_2017_qualification_round/input/kittens.in.txt')
