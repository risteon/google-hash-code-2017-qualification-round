import csv
from .read_input import ProblemInfo
import numpy as np


def write_output(slides, path):
    assert slides.shape[1] == 2
    with open(path, 'w') as file:
        file.write(str(slides.shape[0]))
        file.write('\n')
        for i in range(slides.shape[0]):
            if slides[i, 1] == -1:
                file.write(str(slides[i, 0]))
            else:
                file.write(' '.join(map(str, slides[i, :].tolist())))
            file.write('\n')


class SolutionOutput:
    def __init__(self, problem: ProblemInfo):

        self.problem = problem
        self.state = np.zeros(shape=[problem.cache_count, len(problem.videos)], dtype=np.bool)

    def dump(self):
        print('if cache has video: ', self.state)

    def write_output(self, target="output.txt"):

        with open(target, 'w') as out:
            print("Writing solution to " + target)
            csv_out = csv.writer(out, delimiter=' ')

            num_used_caches = np.count_nonzero(np.any(self.state, axis=-1))

            csv_out.writerow([num_used_caches])

            for i, row in enumerate(self.state):
                if not np.any(row):
                    continue

                lst = []
                for j, x in enumerate(row):
                    if x != 0:
                        lst.append(j)

                csv_out.writerow([i] + lst)
