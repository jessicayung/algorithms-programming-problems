import unittest


class Fibonacci:

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        """Computes the nth Fibonacci number."""
        if n < 0:
            raise Exception("Index was negative. There are no negative-index Fibonacci numbers.")

        # Base cases
        elif n == 0 or n == 1:
            return 1
        # Non-base cases
        elif n in self.memo:
            print("Fetch fib for %i" % n)
            return self.memo[n]

        print("Compute fib %i" % n)
        result = self.fib(n-1) + self.fib(n-2)

        # Memo-ize result
        self.memo[n] = result

        return result


class Tests(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(Fibonacci().fib(10), 89)
        self.assertEqual(Fibonacci().fib(1), 1)
        self.assertEqual(Fibonacci().fib(0), 1)
        self.assertEqual(Fibonacci().fib(5), 8)


if __name__ == '__main__':
    unittest.main()
