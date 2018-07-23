"""
Problem 6:

Find the absolute difference between the sum of the squares of
the first n natural numbers and the square of the sum.

>>> abs_diff(10)
2640

Author: Jessica Yung
Refactored October 2016
"""


# Need abs((1^2+2^2+...+N^2) - (1+2+...+N)^2)


def sum_of_squares(n):
    """Sum of the squares of the first n natural numbers."""
    sum_of_sq = 0
    for i in range(1, n + 1):
        sum_of_sq += i ** 2
    return sum_of_sq


def square_of_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum ** 2


def abs_diff(n):
    return abs(sum_of_squares(n) - square_of_sum(n))
