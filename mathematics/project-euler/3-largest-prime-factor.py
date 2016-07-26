"""
Problem 3: 
Find the largest prime factor of a positive integer n
"""
import math

# Function to find all factors
def factors(n):
	factors = set()
	for i in range(1, int(math.sqrt(n))+1):
		if n % i == 0:
			factors.add(i)
			factors.add(int(n/i))
	return factors

# Function that tests if integers are prime
def isprime(n):
	isprime = True
	if n < 2:
		isprime = False
	elif n > 3:
		for i in range(2, int(math.sqrt(n))+1):
			if n % i == 0:
				isprime = False
				break
	return isprime

# Function that finds largest prime factor
def largest_prime_factor(n):
	primefactors = set()
	for i in factors(n):
		if isprime(i):
			primefactors.add(i)
	if len(primefactors) == 0:
		return "Null"
	else:
		return max(primefactors)

# Read input and solve
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))
