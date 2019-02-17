import csv
from .read_input import ProblemInfo
import numpy as np

class SolutionOutput:
    def __init__(self, problem: ProblemInfo):

        self.problem = problem
        self.state = np.zeros(shape=[problem.cache_count, len(problem.videos)], dtype=np.bool)

    def write_output(self, target="output.txt"):

        with open(target, 'w') as out:
            print("Writing solution to " + target)
            csv_out = csv.writer(out, delimiter=' ')

            num_used_caches = np.count_nonzero(np.any(self.state, axis=-1))

            csv_out.writerow([num_used_caches])

            for i,row in enumerate(self.state):
                if not np.any(row):
                    continue

                csv_out.writerow([i] + [x for x in row[row != 0]])
