import numpy as np


def compute(problem):
    tags_v = problem.vertical_tags
    tags_h = problem.horizontal_tags

    ids_v = problem.vertical_id
    ids_h = problem.horizontal_id

    num_v = np.shape(ids_v)[0]
    num_h = np.shape(ids_h)[0]

    print(num_v)
    print(num_h)
