"""
Problem 2:

Calculate the sum of all even Fibonacci numbers below positive integer n

"""
import unittest

def fib(n):
    """Function to calculate nth Fibonacci number, n being a non-negative integer.
    Def: 0th Fibonacci number is 1.
    """
    if n < 0:
        return "Null"
    elif n == 0 or n == 1:
        return 1
    else:
        f_two_before = 1
        f = 1
        for i in range(2, n+1):
            # Save the value of f for use later
            f_save = f
            f = f + f_two_before
            # Additional print statement for clarity            
            # print(i, "th Fib is ", f)
            f_two_before = f_save
        return f
  

def sum_even_fibs_under_n(n):
    """Calculates sum of even Fibonacci numbers under n."""
    if fib(2) < n:    
        sum = 0    
        i = 2    
        while fib(i) < n:
            sum += fib(i)
            i += 3
        return sum
    else:
        return "Null"

# Tests

class Tests(unittest.TestCase):
    """Tests fib(n)."""

    def __init__(self):
        super(Tests, self).__init__()
        self.nth_fibonacci_test()
        self.sum_even_fibs_under_n_test()


    def nth_fibonacci_test(self):
        # type: () -> Error or not?
        self.assertEqual(fib(0), 1)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(4), 5)

    def sum_even_fibs_under_n_test(self):
        self.assertEqual(sum_even_fibs_under_n(10), 10)
        self.assertEqual(1, 0)

if __name__ == '__main__':
    unittest.main()
#    Tests.nth_fibonacci_test()
#    Tests.sum_even_fibs_under_n_test()

"""
# Read input and solve
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(sum_even_fibs_under_n(n))
"""