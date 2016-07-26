"""
Problem 1: Kangaroo


"""
#!/bin/python3

import sys
import numbers

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

# On move i, k1 will be on x1 + v1*i. k2 will be on x2 + v2*i.
# So we need to check if there is some i for which x1 + v1*i = x2 + v2*i
# That is, if there is a non-negative integer i = (x1-x2)/(v2-v1).

# Watch out for 0 in the denominator!
if (v2-v1) == 0:
    if x1 == x2:
        print("YES")
    else:
        print("NO")
else:
    test = (x1-x2)/(v2-v1)
    if test >= 0 and int(test) == test:
        print("YES")
    else:
        print("NO")

    
#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

"""
Problem 2: Divisible Sum Pairs

You are given an array of n integers a_i, and a positive integer, k. 
Find and print the number of  pairs (i,j) where i < j and  a_i + a_j is evenly divisible by k.
"""

# Cycle through all (i,j) 
# and check if a_i + a_ j (mod k) == 0

count = 0
for j in range(n):
    for i in range(j):
        if (a[i] + a[j]) % k == 0:
            count += 1
print(count)


"""
Problem 3: Angry Professor

A Discrete Mathematics professor has a class of  students. Frustrated with their lack of discipline, he decides to cancel class n if fewer than k students are present when class starts.

Given the arrival time of each student, determine if the class is canceled.
"""

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    students = 0
    for i in range(len(a)):
        if a[i] <= 0:
            students += 1
    if students < k:
        print("YES")
    else:
        print("NO")



"""
Problem 4: Cut the Sticks
You are given n sticks, where the length of each stick is a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

The above step is repeated until no sticks are left.

Given the length of n sticks, print the number of sticks that are left before each subsequent cut operation.
"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# If array length = 0, exit loop
while len(arr) > 0:
    # Output length of array
    print(len(arr))
    # Find min in arr
    minimum = min(arr)
    # Cut each stick by min
    arr[:] = [x - minimum for x in arr]
    # If stick length = 0, remove stick
    deleted = 0
    for i in range(len(arr)):
        # Use i-deleted as index because the length of the array changes when elements are deleted
        if arr[i-deleted] == 0:
            del arr[i-deleted]
            deleted += 1


"""
Problem 5: Non-Divisible Subset
Given a set, S, of n distinct integers, print the size of a maximal subset, S', of S where the sum of any 2 numbers in S' are not evenly divisible by k.
"""

# Read input
n,k = input().strip().split(' ')
n,k = int(n), int(k)
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# (ai + aj) % k != 0 for all (i,j) in the set.
# There should be multiple ways to find such subsets though. E.g. if k = 3 and we have 9 numbers congruent to 1 mod 3 and 10 numbers congruent to 2 mod 3, we should keep all those congruent to 2 mod 3 and none of the numbers congruent to 1 mod 3.
# So do we need to find all such complete subsets and then compare their sizes?
# So there are floor(n/2) pairs of thangs and zeroes. And we need to choose one mod in each pair. 

# If there is more than one element congruent to 0 mod k, then delete all but one of those elements.

# Take out case i = 0
for i in range(1, int(len(arr)/2)):
    # Take out case i = n-i (since we can't have two of e.g. 2 mod 4)
    # Oh ffs we need to treat all cases where n is a multiple of i differently
    # <add code>
    # Define length of array as variable since we'll be referring to it a lot and this will be faster. arrlen is the same for every round of delete operations.
    arrlen = len(arr)
    
    if i != (n-i):
        for j in range(arrlen):
             # count number of elements congruent to i mod k i_mod
            if arr[j] % k == i:
                i_mod += 1
            # count number of elements congruent to (n-i) mod k i_mod_inv
            elif arr[j] % k == (n-i):
                i_mod_inv += 1
        
        if i_mod >= i_mod_inv:
            # delete all elements congruent to (n-i) mod k
            for x in range(arrlen):
                if arr[x] = 
                
        else:
            # delete all elements congruent to i mod k
# count number of elements congrent to 0 mod k zero_mod
if zero_mod > 1:
    # delete all but one element congruent to 0 mod k
            
print(len(arr))

