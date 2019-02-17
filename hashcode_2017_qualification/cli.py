# -*- coding: utf-8 -*-

"""Console script for hashcode_2017_qualification."""
import sys
import click
import os
import numpy as np

from .read_input import parse_input, ProblemInfo
from .solution import solve_for_single_cache
from .write_output import SolutionOutput
from .check_solution import parse_solution, compute_score


def solve_single_cache_dummy(problem, cache_id, current_solution):

    # get all endpoints connected to cache
    ep = problem.endpoints[:, cache_id] != -1
    v = problem.requests[:, ep]
    c = problem.cache_size

    for i in np.nonzero(np.squeeze(v))[0]:
        if problem.videos[i] < c:
            c -= problem.videos[i]
            current_solution.state[cache_id, i] = True

    return current_solution


def solution(problem: ProblemInfo):
    solution = SolutionOutput(problem)
    for i in range(problem.cache_count):
        solution = solve_single_cache_dummy(problem, i, solution)
    return solution


@click.command()
@click.option('--problem', default='kittens.in.txt')
def main(problem):

    solution_functions = [solution]

    problem_obj = parse_input(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                                           'input', problem))

    # problem_obj.dump()

    solutions = [s(problem_obj) for s in solution_functions]

    # calculate scores
    scores = [compute_score(problem_obj, s) for s in solutions]
    print(scores)

    # write all solutions
    for idx, sol in enumerate(solutions):
        sol.write_output(str(idx) + '.txt')

    return 0


@click.command()
@click.option('input', '-i', type=click.File())
@click.option('solution', '-s', type=click.File())
def check_solution(input, solution, args=None):
    task = parse_input(input)
    assert task.cache_count == task.endpoints.shape[1]
    compute_score(task, parse_solution(solution, task.endpoints.shape[1], task.cache_size, task.videos))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
