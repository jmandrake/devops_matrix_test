#!/usr/bin/env python
"""Geocli - A command line interface for the geo tools.
Uses the click library to provide a command line interface
for the geo tools.
"""

import click
from mylib.geotools import get_cities, get_distance


@click.group()
def cli():
    """Geocli - A command line interface for the geo tools.
    Click group allows you to create a group of commands --
    multiple tools."""


@cli.command("distance")
@click.argument("city1", type=str, default="New York, NY")
@click.argument("city2", type=str, default="Los Angeles, CA")
def distance(city1, city2):
    """Get the distance between two cities.
    Usage: ./geocli distance city1 city2
    $ ./geocli distance "New York, NY" "Los Angeles, CA"
    """
    # print(get_distance(city1, city2))
    distance1 = get_distance(city1, city2)
    # print the distance using different colors for cities and distance
    click.secho(f"The distance between {city1}", nl=False, fg="blue")
    click.secho(" and ", nl=False, fg="white")
    click.secho(f"{city2}", nl=False, fg="blue")
    click.secho(" is ", nl=False, fg="white")
    click.secho(f"{distance1:.2f}", nl=False, fg="green")
    click.secho(" miles.\n", nl=False, fg="white")
    # click.echo(f"The distance between {city1} and {city2} is {distance} miles.")


@cli.command("cities")
def cities():
    """Get a list of cities."""
    # print(get_cities())
    cities_list = get_cities()
    for city in cities_list:
        click.secho(f"{city}", nl=False, fg="blue")
        click.secho("\n", nl=False, fg="white")
    click.secho("\n", nl=False, fg="white")


if __name__ == "__main__":
    cli()
