# -*- coding: utf-8 -*-

"""Console script for hashcode_2017_qualification."""
import sys
import click
import os
import numpy as np

from .read_input import parse_input, ProblemInfo
from .write_output import SolutionOutput
from .check_solution import parse_solution, compute_score
from .statistics import compute


def dummy_vertical_mapping(problem_obj):
    return problem_obj.vertical_id.reshape([2, -1])


@click.command()
@click.option('--problem', default='input/a_example.txt')
def main(problem):

    solution_functions = [None]
    problem_obj = parse_input(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                                           problem))

    compute(problem_obj)

    assert problem_obj.vertical_id.shape[0] % 2 == 0
    vertical_mapping = dummy_vertical_mapping(problem_obj)

    # combined_mapping
    n_horiz = problem_obj.horizontal_id.shape[0]
    mapping = np.arange(0, n_horiz + vertical_mapping.shape[0])

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
