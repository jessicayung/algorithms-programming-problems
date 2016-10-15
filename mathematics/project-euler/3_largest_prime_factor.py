"""
Problem 3:

Find the largest prime factor of a positive integer n.

Example:
>>> largest_prime_factor(10)
5

Author: Jessica Yung
Refactored October 2016
"""
import math
import unittest


def factors(n):
    """Find all factors of a positive integer n."""
    factors_of_n = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            factors_of_n.add(i)
            factors_of_n.add(int(n / i))
    return factors_of_n


def is_prime(n):
    """Tests if a positive integer n is prime."""
    is_n_prime = True
    if n < 2:
        is_n_prime = False
    elif n > 3:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                is_n_prime = False
                break
    return is_n_prime


def largest_prime_factor(n):
    """Finds largest prime factor of a positive integer n."""
    prime_factors = set()
    for i in factors(n):
        if is_prime(i):
            prime_factors.add(i)
    if len(prime_factors) == 0:
        return "Null"
    else:
        return max(prime_factors)


class Tests(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(1), "Null")


if __name__ == '__main__':
    unittest.main()
