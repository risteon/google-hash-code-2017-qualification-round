# -*- coding: utf-8 -*-

"""Console script for hashcode_2017_qualification."""
import sys
import click
import os
import numpy as np
import time

from .read_input import parse_input, ProblemInfo
from .write_output import write_output
from .check_solution import parse_solution, compute_score
from .statistics import compute
from .solution import subdivide_and_solve_subproblems
from .combine_vertical_images import combine_vertical_images


def dummy_vertical_mapping(problem_obj):
    v_ids = problem_obj.vertical_id.reshape([-1, 2])
    return v_ids, problem_obj.vertical_tags[:v_ids.shape[0], ...]


def get_time_stamp(with_date=False, with_delims=False):
    if with_date:
        if with_delims:
            return time.strftime('%Y/%m/%d-%H:%M:%S')
        else:
            return time.strftime('%Y%m%d-%H%M%S')
    else:
        if with_delims:
            return time.strftime('%H:%M:%S')
        else:
            return time.strftime('%H%M%S')


@click.command()
@click.option('--problem', default='input/c_memorable_moments.txt')
def main(problem):

    problem_obj = parse_input(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                                           problem))

    # compute(problem_obj)

    assert problem_obj.vertical_id.shape[0] % 2 == 0
    vertical_mapping, merged_tags = combine_vertical_images(problem_obj)

    # combined_mapping
    n_horiz = problem_obj.horizontal_id.shape[0]
    mapping = np.arange(0, n_horiz + vertical_mapping.shape[0])

    def extend(arr, l):
        if l > arr.shape[-1]:
            return np.pad(arr, ((0, 0), (0, l-arr.shape[-1])), 'constant')
        return arr

    l = max(problem_obj.horizontal_tags.shape[-1], merged_tags.shape[-1])

    tags = np.concatenate((extend(problem_obj.horizontal_tags,l), extend(merged_tags,l)))
    solution_ids = subdivide_and_solve_subproblems(tags, mapping)

    horiz_ids = np.stack((problem_obj.horizontal_id,
                        np.full(shape=[problem_obj.horizontal_id.shape[0]], fill_value=-1)), axis=-1)

    input_merged_ids = np.concatenate((horiz_ids, vertical_mapping), axis=0)

    permuted_ids = input_merged_ids[solution_ids]

    problem_name = os.path.basename(problem)[:-4] + '_' + get_time_stamp() + '.txt'
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output', problem_name)
    write_output(permuted_ids, output_path)

    return 0


@click.command()
@click.option('input', '-i')
@click.option('solution', '-s')
def check_solution(input, solution, args=None):
    task = parse_input(input)
    assert task.cache_count == task.endpoints.shape[1]
    compute_score(task, parse_solution(solution, task.endpoints.shape[1], task.cache_size, task.videos, task))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
