"""
Problem 4:

Find the largest palindrome made from the product of two 3-digit integers which is less than positive integer n.

Examples:
>>> greatest_palindromic_product_below_n(10000)
0

>>> greatest_palindromic_product_below_n(111112)
111111

Author: Jessica Yung
Refactored October 2016
"""

def is_palindrome(number):
    """Test if a number is a palindrome."""
    is_a_palindrome = True
    number = str(number)
    for i in range(int(len(number) / 2)):
        if number[i] != number[len(number) - 1 - i]:
            is_a_palindrome = False
            break
    return is_a_palindrome


# Narrow down range
def largest_three_digit_to_consider(n):
    k = 999
    while k * 100 > n:
        k -= 1
    return k


def greatest_palindromic_product_below_n(n):
    """# Systematically go through all relevant products and find the greatest palindrome product."""
    k = largest_three_digit_to_consider(n)
    # Given the palindromic product must be a six-digit number, it must also be a multiple of 11.
    # Thus at least one of the factors must be a multiple of 11.
    l = int(k / 11)
    greatest = 0
    # Let a be the factor that must be a multiple of 11
    for i in range(10, l + 1):
        a = 11 * i
        for j in range(100, k):
            product = a * j
            if product < n:
                if product > greatest:
                    if is_palindrome(product):
                        greatest = product
    return greatest