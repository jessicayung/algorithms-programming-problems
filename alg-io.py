
#!/bin/python3
"""
Input: 
a0 a1 a2
b0 b1 b2
"""
import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
a_score = 0
b_score = 0
tuples = [(a0, b0), (a1, b1), (a2, b2)]

for i in tuples:
    if i[0] != i[1]:
       if i[0] < i[1]:
        b_score += 1
       else:
        a_score += 1

print(a_score, b_score)

"""
Problem 2

int Array input:
6 
-4 3 -9 0 4 1
"""
#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos_count = 0
neg_count = 0
zero_count = 0
for i in arr:
    if i > 0:
        pos_count += 1
    elif i == 0:
        zero_count += 1
    else:
        neg_count += 1

print(pos_count/n)
print(neg_count/n)
print(zero_count/n)

"""
Alt answer to above 1
"""
n = float(raw_input())
lst = [int(x) for x in raw_input().split()]
print format(len([x for x in lst if x > 0])/n, ".6f")
print format(len([x for x in lst if x < 0])/n, ".6f")
print format(len([x for x in lst if x == 0])/n, ".6f")

"""
Alt answer to above 2
"""
n=float(raw_input())
numbers=map(int,raw_input().split())
print round(len([x for x in numbers if x>0])/n,3)
print round(len([x for x in numbers if x<0])/n,3)
print round(len([x for x in numbers if x==0])/n,3)

"""
Problem 3

Printing a hash staircase
"""
n=int(input());[print(" "*(n-i)+'#'*i) for i in range(1,n+1)]

[print(('#' * (i + 1)).rjust(n)) for n in (int(input()),) for i in range(n)]

# I tried
n = int(input().strip())
for i in range(1,n+1):
    print(' '*(n-i), '#'*i)

# but it gave one extra space at the start of each line.
# Changing the last sine to print(' '*(n-i-1), '#'*i) didn't help.


"""
Problem 4

Time converter
"""

time = input().strip()
h = int(time[:2])
# Add 12 to hour of all PM times >= 01:00:00PM
if time[8:] == "PM":
    # 12:00:00PM -> 12:00:00
    if h != 12:
        h += 12
# 12:00:00AM -> 00:00:00
elif h == 12:
    h = '00'
# Make sure e.g. 06:00:00AM comes out as 06:00:00 and not 6:00:00
else:
    h = time[:2]

print(str(h) + time[2:8])

"""
Edge cases involved: 
"""

"""
Problem 5

Right circular array rotation
"""

# Input
n, k, q = input().strip().split(' ')
n, k, q = int(n), int(k), int(q)
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arrnew = arr
# Perform right circular array rotation k times
for i in range(k):
    arr_ref = arr
    for j in range(1,n):
        print("arr before loop: ", arr, "j: ", j)
        # I don't understand why the arr_ref changes after this statement
        arr[j] = arr_ref[j-1] # arrnew = [1,2,3] then arrnew = [1,1,2]
        print(arr, j)
        print("arr_ref after loop: ", arr_ref)
    arr[0] = arr_ref[n-1]
    print(arr_ref)
    arr_ref = arr
    print(arr)
# Query
for i in range(q):
    print(arr[int(input().strip())])


