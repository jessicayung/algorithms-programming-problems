#!/bin/python3

import sys

def breakingRecords(score):
    # Complete this function
    min = score[0]
    max = score[0]
    broke_min = 0
    broke_max = 0
    for s in score[1:]:
        if s < min:
            broke_min += 1
            min = s
        elif s > max:
            broke_max += 1
            max = s
    return broke_max, broke_min
        

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))


