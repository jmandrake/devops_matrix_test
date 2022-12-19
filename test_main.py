"""
Test goes here

"""

from mylib.calculator import add, subtract, multiply, divide
from mylib.geotools import get_cities, get_distance


# create a test for the get_cities function that checks that the output is a list
def test_get_cities():
    assert type(get_cities()) == list


def test_get_distance():
    assert get_distance("New York, NY", "Los Angeles, CA") > 100
    assert get_distance("New York, NY", "Los Angeles, CA") < 4000


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 4) == 1


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(9, 3) == 3
