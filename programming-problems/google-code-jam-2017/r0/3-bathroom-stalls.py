def split(n):
    if n % 2 == 0:
        return [n/2, n/2 - 1]
    elif n % 2 == 1:
        width = n // 2
        return [width, width]
    else:
        return "Error"

def bathroom_stalls(n, k):
    intervals = [n]
    max_min_pair = []
    for i in range(k):
        intervals = sorted(intervals, reverse=True)
        active = intervals[0]
        print("Max: ", active)
        max_min_pair = split(active)
        # TODO: replace active with max_min_pair
        intervals = intervals[1:] + max_min_pair
        print("max_min: ", max_min_pair)
    max_min_pair = [int(j) for j in max_min_pair]
    return max_min_pair

def bathroom_stalls_v2(n, k):
    intervals = [0]*n + [1]
    max_min_pair = []
    active = n
    active_qty = 1
    for i in range(k):
        # 1) while last element is zero, eliminate
        # print("intervals: ", intervals)
        while active_qty == 0:
            # add one or something
            active -= 1
        intervals = intervals[:active+1]
        # print("Max: ", active)
        max_min_pair = split(active)
        # TODO: replace active with max_min_pair
        max = int(max_min_pair[0])
        min = int(max_min_pair[1])
        # Update intervals
        intervals[max] += 1
        intervals[min] += 1
        intervals[active] -= 1
        # print("max_min: ", max_min_pair)
        active_qty -= 1
    max_min_pair = [int(j) for j in max_min_pair]
    return max_min_pair

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  # print("n, k: ", n, k)
  max_min_pair = bathroom_stalls_v2(n, k)
  print("Case #{}: {} {}".format(i, max_min_pair[0], max_min_pair[1]))
  # check out .format's specification for more formatting options