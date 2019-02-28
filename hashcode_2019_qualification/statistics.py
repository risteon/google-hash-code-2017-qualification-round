import click
import os
import sys

from .read_input import parse_input


@click.command()
@click.option('--problem', default='input/a_example.txt')
def main(problem):
    problem_obj = parse_input(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', problem))
    problem_obj.dump()

    # TODO


if __name__ == "__main__":
    sys.exit(main())

