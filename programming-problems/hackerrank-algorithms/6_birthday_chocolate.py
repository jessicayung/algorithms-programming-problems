#!/bin/python3

import sys

def solve(n, s, d, m):
    breaks = 0
    # first m consecutive
    current_sum = 0
    for j in range(m):
        current_sum += s[j]
    if current_sum == d:
        breaks += 1
    for i in range(1,n-(m-1)):
        current_sum += (s[i+m-1] - s[i-1])
        if current_sum == d:
            breaks += 1
    return breaks
            

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
