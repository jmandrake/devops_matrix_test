#!/usr/bin/env python

"""
Main cli or app entry point
"""

from mylib.calculator import add
import click


@click.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    """Add two numbers.

    Args:\n
        a (int)\n
        b (int)\n
    Example:\n
        >>> python main.py add 3 5

    """
    click.echo(add(a, b))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    add_cli()
