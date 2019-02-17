import csv

class SolutionOutput():
    def __init__(self, cache_server_video_mapping=tuple(tuple())):
        self.num_cache_servers = len(cache_server_video_mapping)
        self.cache_server_video_mapping = cache_server_video_mapping


    def write_output(self, target="output.txt"):

        with open(target, 'wb') as out:
            csv_out = csv.writer(out, delimiter=' ')
            csv_out.writerow(self.num_cache_servers)

            for row in self.cache_server_video_mapping:
                csv_out.writerow(row)
