"""Calculate stuff for a right-angled triangle."""

# Enter you module contents here
import math

__version__ = "0.01a"
__author__ = "John Doe"


def hypothenuse(x, y):
    """which returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle"""
    return math.sqrt(x ** 2 + y ** 2)


def area(x, y):
    """which returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters"""
    return 0.5 * x * y
