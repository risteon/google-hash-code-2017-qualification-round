# -*- coding: utf-8 -*-

"""Console script for hashcode_2017_qualification."""
import sys
import click
import os

from .read_input import parse_input
from .solution import solve_utility
from .write_output import SolutionOutput
from .read_input import parse_input
from .check_solution import parse_solution, compute_score


@click.command()
@click.option('--problem', default='kittens.in.txt')
def main(problem):

    solution_functions = [solve_utility]

    problem_obj = parse_input(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'input', problem))

    solutions = [s(problem_obj) for s in solution_functions]

    # Todo write all solutions

    # Todo calculate scores

    for idx, sol in enumerate(solutions):
        out = SolutionOutput(sol)
        out.write_output(str(idx) + '.txt')

    return 0


@click.command()
@click.option('input', '-i', type=click.File())
@click.option('solution', '-s', type=click.File())
def check_solution(input, solution, args=None):
    task = parse_input(input)
    compute_score(task, parse_solution(solution, task.endpoints.shape[1], task.TODOcahcesize, task.videos))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
