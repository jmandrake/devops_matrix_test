"""
Test goes here

"""

from mylib.calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 4) == 1


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(9, 3) == 3
