import numpy as np


def union(tags_a, tags_b):
    return np.shape(np.union1d(tags_a, tags_b))[0]


def condition(tags_a, tags_b):
    num_a = np.shape(tags_a)[0]
    return num_a - union(tags_a, tags_b)


def merge_tags(tag_a, tag_b):
    concat = np.concatenate((tag_a, tag_b))
    concat = concat[concat != 0]
    _, i = np.unique(concat, return_index=True)
    return concat[np.sort(i)]


def compute(problem):
    tags_v = problem.vertical_tags
    tags_h = problem.horizontal_tags

    ids_v = problem.vertical_id
    ids_h = problem.horizontal_id

    num_v = np.shape(ids_v)[0]
    num_h = np.shape(ids_h)[0]

    max_possible_pairs = 2 ^ (num_h + (num_v // 2))
    if num_v == num_h == 0:
        raise ValueError

    for i in range(min(max_possible_pairs, 100)):
        # 0: V, 1: H
        type_a = np.random.randint(low=0, high=1, size=1, dtype=np.bool)
        type_b = np.random.randint(low=0, high=1, size=1, dtype=np.bool)

        if (type_a and num_h == 0) or (not type_a and num_v == 0):
            type_a = not type_a
        if (type_b and num_h == 0) or (not type_b and num_v == 0):
            type_b = not type_b

        if type_a:
            sample_a = tags_h[np.random.randint(low=0, high=num_h-1, size=1)]
        else:
            rand_1 = np.random.randint(low=0, high=num_v-1, size=1)
            rand_2 = np.random.randint(low=0, high=num_v-1, size=1)
            if rand_1 == rand_2:
                rand_2 += 1
            sample_a = merge_tags(tags_v[rand_1], tags_v[rand_2])
        if type_b:
            sample_b = tags_h[np.random.randint(low=0, high=num_h-1, size=1)]
        else:
            rand_1 = np.random.randint(low=0, high=num_v-1, size=1)
            rand_2 = np.random.randint(low=0, high=num_v-1, size=1)
            if rand_1 == rand_2:
                rand_2 += 1
            sample_b = merge_tags(tags_v[rand_1], tags_v[rand_2])

        min_args = np.argmin([union(sample_a, sample_b),
                             condition(sample_a, sample_b),
                             condition(sample_b, sample_a)])

        if min_args == 0:
            print('min for union of a and b')
        elif min_args == 1:
            print('min for a | b')
        elif min_args == 2:
            print('min for b | a')
        else:
            raise ValueError
