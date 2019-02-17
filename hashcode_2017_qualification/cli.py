# -*- coding: utf-8 -*-

"""Console script for hashcode_2017_qualification."""
import sys
import click
import os

from .read_input import parse_input
from .solution import solve_utility


@click.command()
@click.option('--problem', default='kittens.in.txt')
def main(problem):

    solution_functions = [solve_utility]

    problem_obj = parse_input(os.path.join(os.path.realpath(__file__), '..', 'input', problem))

    solutions = [s(problem_obj) for s in solution_functions]

    # Todo write all solutions

    # Todo calculate scores

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
