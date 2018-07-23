"""
You have a function rand7() that generates a random integer from 1 to 7. Use it to write a function rand5() that
generates a random integer from 1 to 5.
"""
import numpy as np


def rand7():
    return int(np.random.random()*7+1)


def rand5():
    result = 7
    while result > 5:
        result = rand7()
    return result


def rand5_v1():
    stop = False

    while stop is False:
        num = rand7()
        if num <= 5:
            return num

# Test rand7():
"""
for i in range(10):
    print(rand7())
"""