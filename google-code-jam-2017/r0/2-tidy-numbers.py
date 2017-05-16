def largest_tidy_number_smaller_than(n):
    # print("n: ", n)
    string_n = list(str(n))
    length_of_n = len(string_n)
    checked_all = False
    changes = 0
    while checked_all == False:
        edited = False
        for index in range(length_of_n-1):
            if edited == False:
                if string_n[index] > string_n[index + 1]:
                    string_n[index] = str(int(string_n[index]) - 1)
                        string_n[remaining_digit] = "9"
                    """
                    if string_n[index] >= string_n[index - 1]:
                        # check applicable
                    """
                    edited = True
                    changes += 1
                    # print("New number: ", string_n)
        if edited == False:
            checked_all = True
    # print("Changes:", changes)
    string_n = ''.join(string_n)
    n = int(string_n)
    # print("Final number: ", n)
    return n

""" Test cases
largest_tidy_number_smaller_than(132)
largest_tidy_number_smaller_than(1000)
largest_tidy_number_smaller_than(7)
largest_tidy_number_smaller_than(11110)
"""

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = input()
  answer = largest_tidy_number_smaller_than(n)
  # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, answer))
  # check out .format's specification for more formatting options