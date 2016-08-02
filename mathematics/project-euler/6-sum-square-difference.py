"""
Problem 6:

Find the absolute difference between the sum of the squares of the first n natural numbers and the square of the sum.

"""

# Need abs((1^2+2^2+...+N^2) - (1+2+...+N)^2)

# Sum of the squares of the first n natural numbers
def sum_of_squares(n):
	sum = 0
	for i in range(1,n+1):
		sum += i**2
	return sum

def square_of_sum(n):
	sum = 0
	for i in range(1, n+1):
		sum += i
	return sum**2

# Read input and solve
t = int(input().strip())
for i in range(t):
	n = int(input().strip())
	print(abs(sum_of_squares(n) - square_of_sum(n)))