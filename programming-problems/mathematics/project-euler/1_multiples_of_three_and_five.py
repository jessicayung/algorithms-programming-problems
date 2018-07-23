"""
Problem 1:

Find the sum of all multiples of 3 or 5 below a positive integer n

Examples:
>>> sum_multiples_3_5(10)
23

>>> sum_multiples_3_5(-1)
0

Author: Jessica Yung
Refactored October 2016
"""


def sum_multiples(n, k):
    """Calculates sum of multiples of k less than n."""
    sum = 0
    if n >= k:
        for i in range(1, int(n/k)):
            sum += k*i
        # It should be range(1,int(n/k)+1) for k such that n % k != 0, so
        if n % k != 0:
            sum += int(n/k)*k
    return sum


def sum_multiples_3_5(n):
    """Calculates sum of all multiples of 3 or 5 below n."""
    return sum_multiples(n, 3) + sum_multiples(n, 5) - sum_multiples(n, 15)
