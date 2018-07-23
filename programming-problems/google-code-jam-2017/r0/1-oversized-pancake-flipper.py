
def k_to_flipper_int(k):
    flipper_int = 0
    for i in range(k):
        flipper_int += 2**i
    # print ("K = ", k, ", flipper_int = ", flipper_int)
    return flipper_int


def string_to_pancakes_int(string, to_int=True):
    binary_string = ""
    for char in string:
        if char == "+":
            binary_string += "0"
        elif char == "-":
            binary_string += "1"
        else:
            return "Error"
    # print("String: ", string)
    if to_int == True:
        num = binary_string_to_int(binary_string)
        # print("Pancake Int: ", num)
        return num
    else:
        # print("Binary string: ", binary_string)
        return binary_string

def binary_string_to_int(string):
    # print("Binary string: ", string)
    binary_string_length = len(string)
    num = 0
    for i in range(1, binary_string_length+1):
        digit = string[-i]
        if digit == "1":
           num += 2**(i-1)
        elif string[-i] == "0":
           pass
        else:
            return "Error"
    # print("Pancake Sequence Int: ", num)
    return num

def largest_power_of_two_smaller_than(n):
    # TODO:
    # print("Largest power of two smaller than ", n, ":")
    power = -1
    while n > 0:
        n = divmod(n, 2)[0]
        power += 1
    if power < 0:
        return "Error: n <= 0"
    power_of_two = 2**power
    # print(power_of_two)
    return power_of_two


def pancake_flipper(pancakes_string, k):
    flipper_int = k_to_flipper_int(k)
    number_of_flips = 0
    pancakes_int = string_to_pancakes_int(pancakes_string)
    if pancakes_int % flipper_int == 0:
        # It is possible
        while pancakes_int != 0:
            pancakes_int -= largest_power_of_two_smaller_than(pancakes_int)
            number_of_flips += 1
        # print ("Number of flips: ", number_of_flips)
        return number_of_flips
    else:
        # print("Impossible")
        return "Impossible"

# k_to_flipper_int(5)
# k_to_flipper_int(10)

def v2_pancake_flipper(pancakes_string, k):
    """O(n2) greedy algorithm.
    Happy side up = 0, empty side up = 1."""
    binary_list = list(string_to_pancakes_int(pancakes_string, to_int=False))
    flips = 0
    # for each distinct possible flip
    for i in range(len(binary_list) - (k-1)):
        # set active as leftmost pancake in flip
        active = binary_list[i]
        # if active is empty side up, flip
        if active == '1':
            # flip this pancake
            binary_list[i] = '0'
            # Flip the next (k-1) pancakes
            for j in range(1,k):
                binary_list[i+j] = str(abs(int(binary_list[i+j]) - 1))
            # print updated pancake list
            # print(binary_list)
            flips += 1
    # After all necessary flips completed
    # if there are still empty side up pancakes, print 'IMPOSSIBLE'
    for i in range(1, k):
        # print("binary_list[-", i, "]: ", binary_list[-i])
        if binary_list[-i] == "1":
            # print("IMPOSSIBLE")
            return "IMPOSSIBLE"
    # print("Flips: ", flips)
    return flips

def v3_pancake_flipper(pancakes_string, k):
    """O(n) greedy algorithm with memo-isation."""
    binary_list = list(string_to_pancakes_int(pancakes_string, to_int=False))
    flips = 0
    flip_count = 0
    n = len(pancakes_string)
    unflip_at = [0] * n
    # for each leftmost pancake
    for i in range(n):
        active = binary_list[i]
        if unflip_at[i] == 1:
            flip_count -= 1
        # if active is empty side up
        if (active == '1' and flip_count % 2 == 0) \
                or (active == '0' and flip_count % 2 == 1):
            # if there is still room to flip, flip
            if i < (n - (k-1)):
                print("Flip ", i)
                # flip this pancake
                flips += 1
                flip_count += 1
                if (i + k) <= n - 1:
                    unflip_at[i + k] += 1
            # if we can't flip, return 'IMPOSSIBLE'
            else:
                print(flip_count, active)
                print("IMPOSSIBLE: -", i)
                return "IMPOSSIBLE"
    # print("Flips: ", flips)
    return flips

# Test cases:
print(v3_pancake_flipper("---+-++-", 3))
print(v2_pancake_flipper("---+-++-", 3))
print(pancake_flipper("---+-++-", 3))
"""
import time

start = time.time()
long_string = "++--++--+++++++--+-+++----+++++++-+---+--+-++--+-" * 19
v2_pancake_flipper(long_string, 8)
end = time.time()
print("Time taken: ", end - start "seconds")
"""

""" For Code Jam
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  pancake_string, k = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
  # print("n, k: ", n, k)
  k = int(k)
  flips = v2_pancake_flipper(pancake_string, k)
  print("Case #{}: {}".format(i, flips))
  # check out .format's specification for more formatting options
"""