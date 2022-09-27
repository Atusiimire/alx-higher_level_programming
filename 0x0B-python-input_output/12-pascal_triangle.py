#!/usr/bin/python3
"""Contains a function called pascal_triangle(...)"""


def pascal_triangle(n):
    """returns a list of lists of integers representing pascal's triangle
    of n"""
    result = []

    if n <= 0:
        return []
