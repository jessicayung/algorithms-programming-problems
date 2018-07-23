# Confirm PEP8 says var[i+1] as opposed to var[i + 1]

def string_to_array(string):
	"""

	"""
	array = []
	for i in range(len(string)):
		array.append(string[i])
	return array

def remove_whitespaces(array):
	for i in range(len(array)):
		if array[i] == ' ':
			del array[i]
	return array

def sort_array(array):
	# Quicksort
	pass

def check_if_perm_of_palindrome(sorted_array):
	"""Checks if a sorted array is a permutation of a palindrome."""
	i = 0
	singles = 0
	while i < len(sorted_array):
		if i == len(sorted_array) - 1:
			if singles == 0:
				return True
			else:
				return False
		elif sorted_array[i] == sorted_array[i+1]:
			i = i + 2
		elif sorted_array[i] != sorted_array[i+1]:
			if singles == 0:
				i = i + 1
			else:
				return False

# Read input
string = str(input())

# Make string an array
array = string_to_array(string)

# Tidy up string by removing whitespaces and making all lower case.
array = remove_whitespaces(array).lower()

# Sort string. E.g. input 'Tact Coa' -> 'aaccott' after this stage.
sorted_array = sort_array(string)

# 
check_if_perm_of_palindrome(sorted_array)