"""
A simple function and a unit test to go with it.

Have tested that this returns no errors with the uncommented tests and that
it returns an AssertionError when the commented (deliberately false) test is included.

Author: Jessica Yung
October 2016
"""

import unittest

def square_x(x):
    """Square X."""
    return x**2

class Tests(unittest.TestCase):
    """Unit test for `square_x` function."""

    def test_square_x(self):
        self.assertEqual(square_x(4), 16)
        self.assertEqual(square_x(10), 100)
#        self.assertEqual(square_x(1), -1)

if __name__ == '__main__':
    unittest.main()