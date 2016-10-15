"""
Problem 4:

Find the largest palindrome made from the product of two 3-digit integers which is less than positive integer n.

"""

# Function to test if a number is a palindrome
def is_palindrome(n):
	is_palindrome = True
	n = str(n)
	for i in range(int(len(n)/2)):
		if n[i] != n[len(n)-1-i]:
			is_palindrome = False
			break
	return is_palindrome

# Narrow range
def largest_three_digit_to_consider(n):
	k = 999
	while k*100 > n:
		k -= 1
	return k

"""
Given the palindromic product must be a six-digit number, it must also be a multiple of 11. Thus at least one of the factors must be a multiple of 11.

"""

# Systematically go through all relevant products and find the greatest palindrome product
def greatest_palindromic_product_below_n(n):
	k = largest_three_digit_to_consider(n)
	l = int(k/11)
	greatest = 0
	# Let a be the factor that must be a multiple of 11
	for i in range(10, l+1):
		a = 11*i
		for j in range(100,k):
			product = a*j
			if product < n:
				if product > greatest:
					if is_palindrome(product):
						greatest = product
	return greatest

# Read input and solve
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(greatest_palindromic_product_below_n(n))
